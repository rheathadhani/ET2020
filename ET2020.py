#ET2020
#Computer Science Project Grade 11

#Importing necessary libraries
import turtle
import random
import math
import platform
import pygame
from time import sleep


#library for sound effects 
from playsound import playsound

#library for bg music
from pygame import mixer

if platform.system()=="Windows":
    try:
        import winsound
    except:
        print("Winsound Module not available to play sound")


#seting up the screen of the game
screen = turtle .Screen()
screen.bgcolor("black")
screen.title("ET 2020")
height=700
width=750
screen.setup(width,height)
screen.bgpic("./images/test.gif")
screen.tracer(0) #shuts off all screen updates

#registering the shapes
screen.register_shape("./images/finalenemy.gif")
screen.register_shape("./images/player.gif")
screen.register_shape("./images/bullet.gif")
screen.register_shape("./images/test.gif")

#initialize the score to 0
score=0

#draw the score
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,275)
scorestring="Score: %s" %score
score_pen.write(scorestring,False,align="left",font=("Arial",14,"normal"))
score_pen.hideturtle()

ins=turtle.Turtle()
ins.speed(0)
ins.pensize(2)
ins.color("white")
ins.penup()
ins.setposition(-290,260)
text="Press left key to move left || Press right key to move right || Press space to shoot"
ins.write(text,False,align="left",font=("Arial",11,"normal"))
ins.hideturtle()

ins1=turtle.Turtle()
ins1.speed(0)
ins1.color("white")
ins1.penup()
ins1.setposition(-290,245)
text1="Aim: Kill all the enemies before it collides with the player."
ins1.write(text1,False,align="left",font=("Arial",11,"normal"))
ins1.hideturtle()

#creating the player
player=turtle.Turtle()
player.color("red")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-280)
player.setheading(90)
player.speed=0 

#number of enemies
number_of_enemies=30
#creating an empty list of enemies
enemies=[]

#add enemies to list
for i in range(number_of_enemies):
    #creating the enemies
    enemies.append(turtle.Turtle())

enemy_start_x=-225
enemy_start_y=220
enemy_number=0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("finalenemy.gif")
    enemy.penup()
    enemy.speed(0)
    x=enemy_start_x+(50*enemy_number)
    y=enemy_start_y
    enemy.setposition(x,y)
    enemy_number+=1
    if enemy_number==10:
        enemy_start_y-=35
        enemy_number=0
    
enemyspeed=0.45

#creating the player's bullet
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("bullet.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed=4

#defining bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate="ready"

#Necessary funcions
#moving the player left and right
def move_left():
    player.speed=-1.5

def  move_right():
    player.speed=1.5

def move_player():
    x=player.xcor()
    x+=player.speed
    if x<-280:
        x=-280
    if x>280:
        x=280    
    player.setx(x)

def fire_bullet():
    play_sound("./audio/laser.wav")
    #variable that needs to be changed
    global bulletstate
    if bulletstate=="ready":
        bulletstate="fire"
        #moving the bullet above player
        x=player.xcor()
        y=player.ycor()
        bullet.setposition(x,y + 10)
        bullet.showturtle()

def is_collision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<35:
        return True
    else:
        return False

def play_sound(sound_file,time=0):
    #windows
    if platform.system()=="Windows":
        winsound.PlaySound(sound_file,winsound.SND_ASYNC)
    #mac
    else:
        os.system("afplay {}&".format(sound_file))

    if time>0:
        turtle.ontimer(lambda:play_sound(sound_file,time),t=int(time*1000))


#binding functions on keyboard keys
screen.listen()
screen.onkeypress(move_left,"Left")
screen.onkeypress(move_right,"Right")
screen.onkeypress(fire_bullet,"space")

#playing a background music
pygame.init()
clock=pygame.time.Clock()
mixer.music.load("./audio/fbackground.wav")
mixer.music.play(-1)

#main game loop
while True:

    #updating the screen activity
    screen.update()

    move_player()
    #moving the bullet
    if bulletstate=="fire":
        y=bullet.ycor()
        y=y+bulletspeed
        bullet.sety(y)

    #check to see if the bullet has gone above the screen
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate="ready"


    for enemy in enemies:
       
        #move the enemy
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)

        #reversing and moving the enemy down
        if enemy.xcor()>280:

            #moves all the enemies down
            for e in enemies:            
                y=e.ycor()
                y-=40
                e.sety(y)
            #change the direction
            enemyspeed*=-1

        if enemy.xcor()<-280:
            #moves all the enemies down
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            #change the direction
            enemyspeed*=-1    

        #check for collision between bullet and enemy
        if is_collision(bullet,enemy):
            play_sound("./audio/explosion.wav")
            #reset bullet
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0,-400)
            #destorying the enemy
            enemy.setposition(0,5000)
            #updating the score
            score+=10
            score_string="Score:%s" %score
            score_pen.clear()
            score_pen.write(score_string,False,align="left",font=("Arial",14,"normal"))

         #check for collision between player and  enemy
        if is_collision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            bullet.hideturtle()
            turtle.resetscreen()
            ins2=turtle.Turtle()
            ins2.speed(0)
            ins2.color("white")
            ins2.penup()
            ins2.setposition(-170,-20)
            text2="Game Over"
            ins2.write(text2,False,align="left",font=("Arial",50,"normal"))
            ins2.hideturtle()
            sleep(5)
            
    

        











