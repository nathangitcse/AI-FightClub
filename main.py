# run 1st source .venv/bin/activate
# run game .venv/bin/python main.py
import pygame
import math

#Fuctions
def turnTowards(currentHeading, targetHeading, turningSpeed,dt):
    targetHeading = targetHeading % 360
    
    turnNeeded = targetHeading - currentHeading
    if turnNeeded > 180:
        turnNeeded -= 360
    elif turnNeeded < -180:
        turnNeeded += 360

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

# base window setup
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # set window size and fullscreen mode
WIDTH, HEIGHT = window.get_size() # get the size of the window
pygame.display.set_caption("AI FightClub") # Title 

clock = pygame.time.Clock() # clock to use later

#Menu = pygame.image.load("img/menuImg.png")
#Menu = pygame.transform.smoothscale(Menu, (WIDTH, HEIGHT))

background = pygame.image.load("img/DesLVL.png") # load background image
background = pygame.transform.rotate(background, 90) # rotate background 90 degrees
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT)) # scale background to fit window

# f18 jet setup
f18Jet = pygame.image.load("img/f18.png") # load f18 jet image
f18Jet = f18Jet.convert_alpha()
f18Jet = pygame.transform.smoothscale(f18Jet, (80, 120)) # convert image to support transparency and scale it

f18Speed = 100 # set speed of f18 jet
f18Heading = 90 # set initial heading of f18 jet, dir by angle.
f18TurningSpeed = 45 # set turning speed of f18 jet
f18x, f18y = WIDTH // 2, HEIGHT // 2 # set initial position of f18 jet

# su-27 jet setup
su27Jet = pygame.image.load("img/su-27.png") # load su-27 jet image
su27Jet = su27Jet.convert_alpha()# convert image to support transparency and scale it
su27Jet = pygame.transform.smoothscale(su27Jet, (80, 120)) 

su27Speed = 100 # set speed of su-27 jet
su27Heading = 90 # set initial heading of su-27 jet, dir by angle.
su27TurningSpeed = 45 # set turning speed of su-27 jet
su27x, su27y = WIDTH // 4, HEIGHT // 2 # set initial position of su-27 jet

gameRunning = True
while gameRunning:
    dt =clock.tick(60) / 1000.0 # limit the game to 60 frames per second and get the time since the last frame in seconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameRunning = False

    #Jet movement
    # Find where su27 is in relation to f18, and set the heading of f18 to point towards su27.
    f18dx = su27x - f18x
    f18dy = su27y - f18y
    f18TargetHeading = math.degrees(math.atan2(f18dy,f18dx))
    f18TargetHeading = f18TargetHeading % 360
    f18Heading = turnTowards(f18Heading, f18TargetHeading, f18TurningSpeed, dt) # update heading of f18 jet based on turning speed and time since last frame

    f18Heading = f18Heading % 360 # keep heading between 0 and 360 degrees

    f18Rad = math.radians(f18Heading) # convert heading to radians
    f18x = f18x+ math.cos(f18Rad) * (f18Speed * dt) # how much of that angle points in x direction, multiply by speed and time to get distance moved in x direction.
    f18y = f18y+ math.sin(f18Rad) * (f18Speed * dt) # how much of that angle points in y direction, multiply by speed and time to get distance moved in y direction.
    
    su27Heading = su27Heading + su27TurningSpeed * dt # update heading of su-27 jet based on turning speed and time since last frame
    su27Heading = su27Heading % 360 # keep heading between 0 and 360 degrees

    su27Rad = math.radians(su27Heading) # convert heading to radians
    su27x = su27x+ math.cos(su27Rad) * (su27Speed * dt) # how much of that angle points in x direction, multiply by speed and time to get distance moved in x direction.
    su27y = su27y+ math.sin(su27Rad) * (su27Speed * dt) # how much of that angle points in y direction, multiply by speed and time to get distance moved in y direction.

    #Rotate jets to match heading
    f18Rotated = pygame.transform.rotate(f18Jet, -f18Heading-90) # rotate f18 jet to match heading
    f18Rect = f18Rotated.get_rect(center=(f18x, f18y)) # get the center of the rotated f18 jet
    su27Rotated = pygame.transform.rotate(su27Jet, -su27Heading-90) # rotate su-27 jet to match heading
    su27Rect = su27Rotated.get_rect(center=(su27x, su27y)) # get the center of the rotated su-27 jet

    #bilt top left conner of window.
    window.blit(background, (0, 0)) # draw background on window
    window.blit(f18Rotated, f18Rect) # draw f18 jet on window
    window.blit(su27Rotated, su27Rect) # draw su-27 jet on window
    pygame.display.flip() # update the display

pygame.quit() # quit pygame when the game loop ends

# FIN lvl background.
# need to add a menu button to allow the user to go back to the main menu from the level background.
# --> also to quit game using excape key
# 0 right, 90 down, 180 left, 270 up