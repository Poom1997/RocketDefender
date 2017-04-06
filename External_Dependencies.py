import pygame
from Game_Settings import *

class Graphics:
    
    def background(x,y):
        gameDisplay.blit(background,(x,y))
        
    def rocketE(x,y):
        gameDisplay.blit(rocketFull,(x,y))

    def rocketD(x,y):
        gameDisplay.blit(rocket3,(x,y))
        
    def rocketC(x,y):
        gameDisplay.blit(rocket2,(x,y))
        
    def rocketB(x,y):
        gameDisplay.blit(rocket1,(x,y))
        
    def rocketA(x,y):
        gameDisplay.blit(rocket0,(x,y))

    def bulletN(x,y):
        gameDisplay.blit(bulletN,(x,y))

    def enemy1(x,y):
        gameDisplay.blit(asteroid,(x,y))

    def enemy2(x,y):
        gameDisplay.blit(asteroid,(x,y))

    def power(x,y):
        gameDisplay.blit(redstar,(x,y))

    def fire(x,y):
        gameDisplay.blit(fireball,(x,y))

class Sounds:
    
    def enemyhit():
        sound = pygame.mixer.Sound("Resources\Sounds\enemyhit.wav")
        sound.play()

    def bullet():
        sound = pygame.mixer.Sound("Resources\Sounds\ibullet.wav")
        sound.play()

    def mainSound():
        global mainsound
        mainsound = pygame.mixer.Sound("Resources\Sounds\mainsound.wav")
        mainsound.set_volume(0.5)
        mainsound.play(loops = -1)

    def mainSoundSTOP():
        mainsound.stop()

    def menuSound():
        global menusound
        menusound = pygame.mixer.Sound("Resources\Sounds\menusound.wav")
        menusound.set_volume(0.3)
        menusound.play(loops = -1)

    def menuSoundSTOP():
        menusound.stop()

    def powerup():
        pwrsound = pygame.mixer.Sound("Resources\Sounds\Powerup.wav")
        pwrsound.set_volume(0.5)
        pwrsound.play()
        
    def powerdown():
        sound = pygame.mixer.Sound("Resources\Sounds\Powerdown.wav")
        sound.play()

    def death():
        sound = pygame.mixer.Sound("Resources\Sounds\Death.wav")
        sound.play()

    def highscore():
        sound = pygame.mixer.Sound("Resources\Sounds\Score.wav")
        sound.play()

    def challenge():
        sound = pygame.mixer.Sound("Resources\Sounds\Challenge.wav")
        sound.play()

    def buttonover():
        sound = pygame.mixer.Sound("Resources\Sounds\over.wav")
        sound.play()
        
    def buttonclick():
        click = pygame.mixer.Sound("Resources\Sounds\click.wav")
        click.set_volume(0.5)
        click.play()
