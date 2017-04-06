import pygame
from Objects_Dependencies import *
from External_Dependencies import *
from Game_Settings import *

#Menu Class
class Menu:
    def __init__(self):
        Sounds.menuSound()
    def main_Loop(self):
        menu = True
        pos =1
        while(menu):
            #Event Handling
            x,y = pygame.mouse.get_pos()
            a,b,c = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    quit()
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    quit()

            #Mouse Detection and interaction
            if(pos==1):
                gameDisplay.blit(menu1,(0,0))
                if(x>580 and x <740 and y >350 and y < 380):
                    gameDisplay.blit(menuplay,(0,0))
                    if(a==1):
                        Sounds.buttonclick()
                        pos = 2
                if(x>575 and x <750 and y >405 and y < 470):
                    gameDisplay.blit(menureset,(0,0))
                    if(a==1):
                        Sounds.buttonover()
                        pos=3
                if(x>560 and x <775 and y >485 and y < 515):
                    gameDisplay.blit(menucredit,(0,0))
                    if(a==1):
                        Sounds.buttonover()
                        pos=4
                if(x>610 and x <730 and y >540 and y < 570):
                    gameDisplay.blit(menuquit,(0,0))
                    if(a==1):
                        Sounds.buttonclick()
                        pygame.quit()
                        quit()
            if(pos==2):
                gameDisplay.blit(instruction,(0,-30))
                if(x>440 and x <635 and y >380 and y < 415):
                    if(a==1):
                        Sounds.buttonclick()
                        Sounds.menuSoundSTOP()
                        m=Main()
                        m.main_Loop()
                    gameDisplay.blit(instructionplay,(0,-30))
                if(x>480 and x <575 and y >430 and y < 450):
                    gameDisplay.blit(instructionquit,(0,-30))
                    if(a==1):
                        Sounds.buttonover()
                        pos = 1
            if(pos==3):
                gameDisplay.blit(highscorereset,(0,0))
                if(x>100 and x <290 and y >435 and y < 455):
                    if(a==1):
                        Sounds.buttonclick()
                        s=Highscore(0)
                        s.writefile()
                        pos=1
                    gameDisplay.blit(highscoreresetyes,(0,0))
                if(x>330 and x <505 and y >435 and y < 455):
                    if(a==1):
                        Sounds.buttonover()
                        pos=1
                    gameDisplay.blit(highscoreresetno,(0,0))

            if(pos==4):
                gameDisplay.blit(credit,(0,0))
                if(x>320 and x <470 and y >555 and y < 585):
                    if(a==1):
                        Sounds.buttonover()
                        pos=1
                    gameDisplay.blit(creditback,(0,0))
                
            pygame.display.update()
            clock.tick(100)
            
#Game Class
class Main:
    def __init__(self):
        Sounds.mainSound()
        self.x=(display_width * 0.45)
        self.y=(display_height * 0.80)
        self.x_move = 0
        self.enemy = Enemy('Asteroid')
        self.enemyx,self.enemyy,self.enemyspeed,self.enemywidth,self.enemyheight = self.enemy.size()
        self.power= PowerUP('PowerStar')
        self.powerx,self.powery,self.powerspeed,self.powerwidth,self.powerheight = self.power.size()
        self.fire= Fireball('FireBall')
        self.firex,self.firey,self.firespeed,self.firewidth,self.fireheight = self.fire.size()
        self.bullety = 0
        self.bulletx = 0
        self.bulletwidth = 0
        self.bulletheight = 0
        self.score = 0
        self.lives = 4
        self.kill = False
        self.onebullet = True
        self.challenge = False
        self.shoot = False
        self.PLAY=True
        self.alarmscore = True
        self.i=0
        s=Highscore(self.score)
        self.hiscore = int(s.readfile())
        
    def main_Loop(self):
        #Event Handling
        while(self.PLAY):
            self.i=self.i+1
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    s=Highscore(self.hiscore)
                    s.writefile()
                    pygame.quit()
                    quit()
                if(event.type==pygame.KEYDOWN):
                    if(event.key ==pygame.K_DELETE):
                        s=Highscore(self.hiscore)
                        s.writefile()
                        pygame.quit()
                        quit()
                    if(event.key ==pygame.K_ESCAPE):
                        self.lives = 0
                    if(event.key==pygame.K_LEFT):
                        self.x_move=-10
                    if(event.key==pygame.K_RIGHT):
                        self.x_move=10
                    if(event.key==pygame.K_SPACE):
                        if(self.onebullet==True):
                            Sounds.bullet()
                            self.bullet = Bullet('bulletNormal')
                            self.bulletx,self.bullety,self.bulletspeed,self.bulletwidth,self.bulletheight = self.bullet.size(display_width,self.x,self.y)
                            self.shoot = True
                            self.onebullet = False
                        
                if(event.type==pygame.KEYUP):
                    if(event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
                        self.x_move=0

                #Challenge Mode
                if(self.score >=20 and self.challenge == False):
                    self.challenge = True
                    Sounds.challenge()

            #Graphics
            self.x=self.x+self.x_move
            gameDisplay.blit(background,(0,0))
            if(self.shoot):
                gameDisplay.blit(bulletN,(self.bulletx,self.bullety))
                self.bullety -=self.bulletspeed 
            Graphics.enemy1(self.enemyx,self.enemyy)
            self.enemyy +=self.enemyspeed
            Graphics.power(self.powerx,self.powery)
            self.powery +=self.powerspeed
            if(self.challenge):
                Graphics.fire(self.firex,self.firey)
                self.firey +=self.firespeed
                Text.challengenotify()

            #Rocket
            if(self.lives == 4):
                Graphics.rocketE(self.x,self.y)
            if(self.lives == 3):
                Graphics.rocketD(self.x,self.y)
            if(self.lives == 2):
                Graphics.rocketC(self.x,self.y)
            if(self.lives == 1):
                Graphics.rocketB(self.x,self.y)
            if(self.lives == 0):
                Graphics.rocketA(self.x,self.y)
                self.lives = self.lives - 1

            #Difficulty
            Text.difficulty()
            if(self.enemyspeed <=3):
                gameDisplay.blit(lvl1,(display_width/2-10,22))
            if(self.enemyspeed <=5.5 and self.enemyspeed >3):
                gameDisplay.blit(lvl2,(display_width/2-20,22))
            if(self.enemyspeed <7.5 and self.enemyspeed >5.5):
                gameDisplay.blit(lvl3,(display_width/2-30,22))
            if(self.enemyspeed >=7.5):
                gameDisplay.blit(lvlpro,(display_width/2-50,22))
                
            #Score, Highscore, and Instructions
            Text.score(self.score)
            if(self.hiscore!=0):
                Text.highScore(self.hiscore)
            if(self.hiscore<=self.score):
                self.hiscore = self.score
                if(self.hiscore>0 and self.hiscore <= self.score):
                    if(self.alarmscore):
                        Sounds.highscore()
                        self.alarmscore = False
                    Text.highScoreBeaten(self.hiscore)
            if(self.score<2):
                Text.reminder("Press ESC - Surrender and return to main menu")
                Text.reminder2("Use arrow keys to move / Spacebar to Shoot")
                
            #Stop Rocket
            if(self.x>display_width-rocket_width or self.x<0):
                self.x_move = 0
                
            #Bullet
            if(self.bullety>self.enemyy-self.enemyheight and self.bullety<self.enemyy):
                if(self.bulletx>self.enemyx and self.bulletx<self.enemyx+self.enemywidth or \
                   self.bulletx+self.bulletwidth<self.enemyx+self.enemywidth\
                   and self.bulletx+self.bulletwidth >self.enemyx):
                    self.shoot = False
                    self.bullety = display_width-50
                    self.kill=True

            if(self.bullety < -self.bulletheight or self.kill == True):
                self.onebullet = True
                self.bulletx,self.bullety= self.bullet.refresh()
                
            #Enemy                   
            if(self.y<self.enemyy+self.enemyheight and self.y>self.enemyy-self.enemyheight+10):
                if(self.x>self.enemyx and self.x<self.enemyx+self.enemywidth or \
                   self.x+rocket_width>self.enemyx and self.x+rocket_width<\
                   self.enemyx+self.enemywidth):
                    if(self.lives!=1):
                        Sounds.powerdown()
                    self.lives = self.lives - 1
                    self.enemyx,self.enemyy,self.enemyspeed = self.enemy.refresh()

            if(self.enemyy> display_height or self.kill == True):
                if(self.kill==True):
                    Sounds.enemyhit()
                    self.score +=1
                if(self.enemyy> display_height):
                    if(self.lives!=1):
                        Sounds.powerdown()
                    self.score -=5
                    self.lives -=1
                self.kill = False
                self.enemyx,self.enemyy,self.enemyspeed = self.enemy.refresh()
                 
            #PowerUp     
            if(self.y<self.powery+self.powerheight and self.y>self.powery-self.powerheight):
                if(self.x>self.powerx and self.x<self.powerx+self.powerwidth or \
                   self.x+rocket_width>self.powerx and self.x+rocket_width<\
                   self.powerx+self.powerwidth):
                    Sounds.powerup()
                    if(self.lives < 4):
                        self.lives += 1
                    self.score+=5
                    self.powerx,self.powery,self.powerspeed = self.power.refresh()

            if(self.powery> display_height):
                 self.powerx,self.powery,self.powerspeed = self.power.refresh()

            #Fireball
            if(self.challenge):
                if(self.y<self.firey+self.fireheight and self.y>self.firey-self.fireheight):
                    if(self.x>self.firex and self.x<self.firex+self.firewidth or \
                       self.x+rocket_width+10>self.firex and self.x+rocket_width<\
                       self.firex+self.firewidth):
                        self.lives = 0
                        self.firex,self.firey,self.firespeed = self.fire.refresh()
                        
                if(self.firey> display_height):
                    self.firex,self.firey,self.firespeed = self.fire.refresh()

            #Death
            if(self.lives == -1):
                Sounds.mainSoundSTOP()
                Sounds.death()
                s=Highscore(self.hiscore)
                s.writefile()
                Text.crashMessage()
      
            pygame.display.update()
            clock.tick(120)
