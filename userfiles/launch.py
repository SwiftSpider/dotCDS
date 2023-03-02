import turtle
import os

wn = turtle.Screen()
wn.title("Official Game Launcher")
wn.setup(width=1220,height=820)
wn.bgcolor("gray")

snekpn = turtle.Turtle()
snekpn.penup()
snekpn.hideturtle()
snekpn.goto(-525,370)
snekpn.write("Snake Game", align="center", font=("Courier New", 14, "normal"))

snekbt = turtle.Turtle()
snekbt.penup()
snekbt.clear()
snekbt.shape("square")
snekbt.color("blue")
snekbt.goto(-525,360)

birbpn = turtle.Turtle()
birbpn.penup()
birbpn.hideturtle()
birbpn.goto(-525,310)
birbpn.write("Flappy Bird", align="center", font=("Courier New", 14, "normal"))

birbbt = turtle.Turtle()
birbbt.penup()
birbbt.clear()
birbbt.shape("square")
birbbt.color("blue")
birbbt.goto(-525,300)

dinopn = turtle.Turtle()
dinopn.penup()
dinopn.hideturtle()
dinopn.goto(-350,370)
dinopn.write("Offline Dino", align="center", font=("Courier New", 14, "normal"))

dinobt = turtle.Turtle()
dinobt.penup()
dinobt.clear()
dinobt.shape("square")
dinobt.color("blue")
dinobt.goto(-350,360)

starpn = turtle.Turtle()
starpn.penup()
starpn.hideturtle()
starpn.goto(-340,310)
starpn.write("Ships n' Sruff", align="center", font=("Courier New", 14, "normal"))

starbt = turtle.Turtle()
starbt.penup()
starbt.clear()
starbt.shape("square")
starbt.color("blue")
starbt.goto(-350,300)

minepn = turtle.Turtle()
minepn.penup()
minepn.hideturtle()
minepn.goto(-350,260)
minepn.write("Minesweeper", align="center", font=("Courier New", 14, "normal"))

minebt = turtle.Turtle()
minebt.penup()
minebt.clear()
minebt.shape("square")
minebt.color("blue")
minebt.goto(-350,250)

def runSnek(x,y):
    os.system("python3 userfiles/Games/SnakeGame.py")

def runDino(x,y):
    os.system("python3 userfiles/Games/OfflineDino.py")

def runFlap(x,y):
    os.system("python3 userfiles/Games/Flappy.py")

def runStar(x,y):
    os.system("python3 userfiles/Games/Startrek.py")

def runMine(x,y):
    os.system("python3 userfiles/Games/minesweep.py")

dinobt.onclick(runDino)
birbbt.onclick(runFlap)
snekbt.onclick(runSnek)
starbt.onclick(runStar)
minebt.onclick(runMine)

#upper right (600,400)
#lower left (-595,-390)

wn.mainloop()