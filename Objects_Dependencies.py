import abc
import pygame
import Main
import time
import random
from Game_Settings import *

class Objects(metaclass=abc.ABCMeta):
    def __init__(self,name):
        self.name = name
    @abc.abstractmethod
    def size(self):
        pass

class Score(metaclass=abc.ABCMeta):
    def __init__(self,score):
        self.score = score
        
    @abc.abstractmethod
    def readfile(self):
        pass
    
    @abc.abstractmethod
    def writefile(self):
        pass

class Enemy(Objects):
    def __init__ (self,name):
        super().__init__(name)

    def size(self):
        objectstarty = -600
        objectspeed = 2
        objectwidth = 100
        objectheight = 95
        self.speed = objectspeed
        self.objectx = objectwidth
        objectstartx = random.randrange(0,display_width-self.objectx+20)
        return (objectstartx,objectstarty,self.speed,objectwidth,objectheight)
    def refresh(self):
        objectstartx = random.randrange(0,display_width-self.objectx+20)
        objectstarty = -600
        if(self.speed<9):
            self.speed = self.speed + 0.1
        else:
            self.speed = self.speed
        return (objectstartx,objectstarty,self.speed)

class Fireball(Objects):
    def __init__ (self,name):
        super().__init__(name)

    def size(self):
        objectstartx = random.randrange(0,display_width)
        objectstarty = -900
        objectspeed = 8
        objectwidth = 52
        objectheight = 46
        self.speed = objectspeed
        self.objectx = objectwidth
        return (objectstartx,objectstarty,self.speed,objectwidth,objectheight)
    def refresh(self):
        objectstartx = random.randrange(0,display_width-self.objectx)
        objectstarty = -900
        self.speed = self.speed
        return (objectstartx,objectstarty,self.speed)


class Bullet(Objects):
    def __init__ (self,name):
        super().__init__(name)

    def size(self,display_width,xposition,yposition):
        objectstartx = xposition + 10
        objectstarty = yposition - rocket_height/2
        objectspeed = 10
        objectwidth = 50
        objectheight = 50
        self.speed = objectspeed
        self.objectx = objectwidth
        return (objectstartx,objectstarty,self.speed,objectwidth,objectheight)
    
    def refresh(self):
        objectstartx = -50
        objectstarty = 0
        return (objectstartx,objectstarty)

class PowerUP(Objects):
    def __init__ (self,name):
        super().__init__(name)

    def size(self):
        objectstartx = random.randrange(0,display_width)
        objectstarty = -random.randrange(9000,17000,3)
        objectspeed = 5
        objectwidth = 65
        objectheight = 32
        self.speed = objectspeed
        self.objectx = objectwidth
        return (objectstartx,objectstarty,self.speed,objectwidth,objectheight)
    
    def refresh(self):
        objectstartx = random.randrange(0,display_width-self.objectx+20)
        objectstarty = objectstarty = -random.randrange(5000,12000,3)
        self.speed = self.speed
        return (objectstartx,objectstarty,self.speed)

class Text:
    def crashText_objects(text,font):
        TextSurface=font.render(text,True,dGrey)
        return TextSurface, TextSurface.get_rect()
    def crashMessage_display(text):
        CAPS=pygame.font.Font('freesansbold.ttf',100)
        TextSurf,TextRect = Text.crashText_objects(text,CAPS)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(5)
        m=Main.Menu()
        m.main_Loop()
    def crashMessage():
        Text.crashMessage_display('Game Over')
    def score(count):
        font = pygame.font.SysFont(None,25)
        if(count<0):
            text = font.render("Score:"+str(count)+"  NEGATIVE!!!",True,red)
        else:
            text = font.render("Score:"+str(count),True,white)
        gameDisplay.blit(text,(5,5))
    def challengenotify():
        font = pygame.font.SysFont(None,20)
        text = font.render("CHALLENGE MODE!",True,green)
        gameDisplay.blit(text,(display_width - 135,5))
    def highScore(highscore):
        font = pygame.font.SysFont(None,20)
        text = font.render("HighScore:"+str(highscore),True,red)
        gameDisplay.blit(text,(5,22))
    def highScoreBeaten(highscore):
        font = pygame.font.SysFont(None,20)
        text = font.render("HighScore:"+str(highscore),True,green)
        gameDisplay.blit(text,(5,22))
        text2 = font.render("New HighScore!",True,orange)
        gameDisplay.blit(text2,(display_width -110,22))
    def difficulty():
        font = pygame.font.SysFont(None,20)
        text = font.render("Difficulty",True,bblue)
        gameDisplay.blit(text,(display_width/2-30,5))
    def reminder(message):
        font = pygame.font.SysFont(None,25)
        text = font.render(message,True,green)
        gameDisplay.blit(text,(5,38))
    def reminder2(message):
        font = pygame.font.SysFont(None,25)
        text = font.render(message,True,yellow)
        gameDisplay.blit(text,(5,55))

class Highscore(Score):
    def __init__(self,score):
        super().__init__(score)

    def readfile(self):
        try:
            infile=open("records.rkd","r")
            rd = infile.readline()
            highscore = int(rd)
            infile.close()
            return highscore
        except IOError:
            outfile=open("records.rkd","w")
            outfile.write('0')
            outfile.close()
            return 0
        
    def writefile(self):
        outfile=open("records.rkd","w")
        outfile.write(str(self.score))
        outfile.close()
