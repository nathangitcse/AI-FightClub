# run 1st source .venv/bin/activate
# run game .venv/bin/python main.py
import pygame

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

f18Jet = pygame.image.load("img/f18.png") # load f18 jet image
f18Jet = f18Jet.convert_alpha()
f18Jet = pygame.transform.smoothscale(f18Jet, (80, 120)) # convert image to support transparency and scale it
f18Speed = 100 # set speed of f18 jet
f18x, f18y = WIDTH // 2, HEIGHT // 2 # set initial position of f18 jet

su27Jet = pygame.image.load("img/su-27.png") # load su-27 jet image
su27Jet = su27Jet.convert_alpha()# convert image to support transparency and scale it
su27Jet = pygame.transform.smoothscale(su27Jet, (80, 120)) 
su27Speed = 100 # set speed of su-27 jet
su27x, su27y = WIDTH // 4, HEIGHT // 2 # set initial position of su-27 jet

GameRunning = True
while GameRunning:
    dt =clock.tick(60) / 1000.0 # limit the game to 60 frames per second and get the time since the last frame in seconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GameRunning = False

    #Jet movement
    f18x = f18x + (f18Speed * dt)
    su27x = su27x + (su27Speed * dt)

    #bilt top left conner of window.
    window.blit(background, (0, 0)) # draw background on window
    window.blit(f18Jet, (f18x, f18y)) # draw f18 jet on window
    window.blit(su27Jet, (su27x, su27y)) # draw su-27 jet on window
    pygame.display.flip() # update the display

pygame.quit() # quit pygame when the game loop ends

# FIN lvl background.
# need to add a menu button to allow the user to go back to the main menu from the level background.
# --> also to quit game using excape key