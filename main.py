# run 1st source .venv/bin/activate
# run game .venv/bin/python main.py
# headings: 0 right, 90 down, 180 left, 270 up
import pygame
import math

# Functions
# Turn a heading toward a target, by at most turningSpeed degrees per second.
def turnTowards(currentHeading, targetHeading, turningSpeed,dt):
    targetHeading = targetHeading % 360

    # take the shorter way around the circle
    turnNeeded = targetHeading - currentHeading
    if turnNeeded > 180:
        turnNeeded -= 360
    elif turnNeeded < -180:
        turnNeeded += 360

    # turn as far as allowed this frame, or snap if already close
    maxTurn = turningSpeed * dt
    if turnNeeded > maxTurn:
        currentHeading += maxTurn
    elif turnNeeded < -maxTurn:
        currentHeading -= maxTurn
    else:
        currentHeading = targetHeading

    currentHeading = currentHeading % 360

    return currentHeading

pygame.init()

# window setup
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # fullscreen at screen size
WIDTH, HEIGHT = window.get_size()
pygame.display.set_caption("AI FightClub")

clock = pygame.time.Clock()

#Menu = pygame.image.load("img/menuImg.png")
#Menu = pygame.transform.smoothscale(Menu, (WIDTH, HEIGHT))

# background: load, turn sideways, stretch to fit window
background = pygame.image.load("img/DesLVL.png")
background = pygame.transform.rotate(background, 90)
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

# f18 jet setup
f18Jet = pygame.image.load("img/f18.png")
f18Jet = f18Jet.convert_alpha() # keep transparent background
f18Jet = pygame.transform.smoothscale(f18Jet, (80, 120))

f18Speed = 100 # pixels per second
f18Heading = 90 # degrees
f18TurningSpeed = 45 # degrees per second
f18x, f18y = WIDTH // 2, HEIGHT // 2 # start position (center of jet)

# su-27 jet setup (same as f18)
su27Jet = pygame.image.load("img/su-27.png")
su27Jet = su27Jet.convert_alpha()
su27Jet = pygame.transform.smoothscale(su27Jet, (80, 120))

su27Speed = 100
su27Heading = 90
su27TurningSpeed = 45
su27x, su27y = WIDTH // 4, HEIGHT // 2

# Trails: each jet keeps a list of its recent (x, y) positions
TRAILMAXLENGTH = 120 # points kept (about 2 seconds at 60 FPS)
TRAILWIDTH = 4 # line thickness in pixels

f18Trail = []
f18Trail.append((f18x, f18y))
f18Trail.pop(0)

su27Trail = []
su27Trail.append((su27x, su27y))
su27Trail.pop(0)

# Colors (r, g, b)
BLUE = (80,160,255)
RED = (255,80,80)

# Aim line: how far it sticks out in front of each jet
LAZERLENGTH = 120 # pixels

gameRunning = True
while gameRunning:
    dt =clock.tick(60) / 1000.0 # cap at 60 FPS; seconds since last frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameRunning = False

    # Jet movement
    # f18: aim at su27, turn toward it, then move forward
    f18dx = su27x - f18x
    f18dy = su27y - f18y
    f18TargetHeading = math.degrees(math.atan2(f18dy,f18dx))
    f18TargetHeading = f18TargetHeading % 360
    f18Heading = turnTowards(f18Heading, f18TargetHeading, f18TurningSpeed, dt)
    f18Heading = f18Heading % 360

    # save position for the trail, drop the oldest point if too long
    f18Trail.append((f18x, f18y))
    if len(f18Trail) > TRAILMAXLENGTH:
        f18Trail.pop(0)

    # split heading into x and y parts, times distance this frame
    f18Rad = math.radians(f18Heading)
    f18x = f18x+ math.cos(f18Rad) * (f18Speed * dt)
    f18y = f18y+ math.sin(f18Rad) * (f18Speed * dt)

    # su27: same steps, aiming at f18
    su27dx = f18x - su27x
    su27dy = f18y - su27y
    su27TargetHeading = math.degrees(math.atan2(su27dy,su27dx))
    su27TargetHeading = su27TargetHeading % 360
    su27Heading = turnTowards(su27Heading,su27TargetHeading,su27TurningSpeed, dt)
    su27Heading = su27Heading % 360

    su27Trail.append((su27x, su27y))
    if len(su27Trail) > TRAILMAXLENGTH:
        su27Trail.pop(0)

    su27Rad = math.radians(su27Heading)
    su27x = su27x+ math.cos(su27Rad) * (su27Speed * dt)
    su27y = su27y+ math.sin(su27Rad) * (su27Speed * dt)

    # Rotate jets to match heading (image points up, so offset by 90)
    # rect keeps each jet centered on its x, y
    f18Rotated = pygame.transform.rotate(f18Jet, -f18Heading-90)
    f18Rect = f18Rotated.get_rect(center=(f18x, f18y))
    su27Rotated = pygame.transform.rotate(su27Jet, -su27Heading-90)
    su27Rect = su27Rotated.get_rect(center=(su27x, su27y))

    # Aim line end point: LAZERLENGTH pixels ahead of each nose
    f18LazerEndX = f18x + math.cos(f18Rad) * LAZERLENGTH
    f18LazerEndY = f18y + math.sin(f18Rad) * LAZERLENGTH
    su27LazerEndX = su27x + math.cos(su27Rad) * LAZERLENGTH
    su27LazerEndY = su27y + math.sin(su27Rad) * LAZERLENGTH
    

    # Draw (each layer covers the one before): background, trails, aim lines, jets
    window.blit(background, (0, 0))

    if (len(f18Trail) > 1) and (len(su27Trail) > 1): # a line needs 2+ points
        pygame.draw.lines(window, BLUE, False, f18Trail, TRAILWIDTH)
        pygame.draw.lines(window, RED, False, su27Trail, TRAILWIDTH)
        
    pygame.draw.line(window, BLUE, (f18x, f18y), (f18LazerEndX, f18LazerEndY), 3)
    pygame.draw.line(window, RED, (su27x, su27y), (su27LazerEndX, su27LazerEndY), 3)
    window.blit(f18Rotated, f18Rect)
    window.blit(su27Rotated, su27Rect)
    pygame.display.flip() # show the new frame

pygame.quit()

# TODO: menu button to go back to the main menu from the level
# DONE: quit game with escape key
