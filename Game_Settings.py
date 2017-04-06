import pygame

#Initalization#
pygame.init()
display_width = 800
display_height = 600
rocket_width = 68
rocket_height = 89

#Color#
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
dGrey =(200,200,200)
orange =(252,212,64)
bblue = (16,200,205)
yellow = (225,225,0)

#Setup
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Rocket Defender 1.0')
clock=pygame.time.Clock()
background=pygame.image.load('Resources\Images\Background.png')
rocketFull=pygame.image.load('Resources\Images\Rocket Full.png')
rocket3=pygame.image.load('Resources\Images\Rocket 3-4.png')
rocket2=pygame.image.load('Resources\Images\Rocket 2-4.png')
rocket1=pygame.image.load('Resources\Images\Rocket 1-4.png')
rocket0=pygame.image.load('Resources\Images\Rocket 0-4.png')
bulletN=pygame.image.load('Resources\Images\BulletN.png')
asteroid = pygame.image.load('Resources\Images\iasteroid.png')
redstar = pygame.image.load('Resources\Images\iredstar.png')
fireball = pygame.image.load('Resources\Images\ifireball.png')
lvl1 = pygame.image.load('Resources\Images\L1.png')
lvl2 = pygame.image.load('Resources\Images\L2.png')
lvl3 = pygame.image.load('Resources\Images\L3.png')
lvlpro = pygame.image.load('Resources\Images\LPRO.png')
menu1 = pygame.image.load('Resources\Images\menu.png')
menuplay = pygame.image.load('Resources\Images\menu1.png')
menureset = pygame.image.load('Resources\Images\menu2.png')
menucredit = pygame.image.load('Resources\Images\menu3.png')
menuquit = pygame.image.load('Resources\Images\menu4.png')
instruction = pygame.image.load('Resources\Images\instructions.png')
instructionplay = pygame.image.load('Resources\Images\instructionsplay.png')
instructionquit = pygame.image.load('Resources\Images\instructionsquit.png')
highscorereset = pygame.image.load('Resources\Images\highscorereset.png')
highscoreresetyes = pygame.image.load('Resources\Images\highscoreresetproceed.png')
highscoreresetno = pygame.image.load('Resources\Images\highscoreresetcancel.png')
credit = pygame.image.load('Resources\Images\credit.png')
creditback = pygame.image.load('Resources\Images\creditback.png')
icon = pygame.image.load('Resources\Images\iasteroidIcon.png')
pygame.display.set_icon(icon)
