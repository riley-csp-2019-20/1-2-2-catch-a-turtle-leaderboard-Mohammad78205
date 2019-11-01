#a121_catch_a_turtle.py
#------import statements------
import leaderboard as lb
import turtle as trtl
import random
 
#------gane configuration-----
turtleshape= "turtle"
turtlecolor= "purple"
turtlesize = 7

score = 0

timer = 5
counter_interval = 1000 
timer_up = False

#------Scoreboard variables------
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name")

#------initialize turtle------
Shelldon = trtl.Turtle(shape=turtleshape)
Shelldon.speed(0)
Shelldon.color(turtlecolor)
Shelldon.shapesize(turtlesize)
#------game functions---------
def turtle_clicked(x,y):
   print("Shelldon get clicked")
   change_position()
   update_score()
 
def update_score():
    Score_Display.pencolor("black")
    global score
    score += 1
    print(score)
    Score_Display.clear()
    Score_Display.write(score, font = font_setup)
    if score == 5:
        turtlecolor = "red"
        Shelldon.color(turtlecolor)
 
def change_position():
    Shelldon.penup()
    Shelldon.ht()
    if not timer_up:
        Shelldonx = random.randint(-350,280)
        Shelldony = random.randint(-300,300)
        Shelldon.goto(Shelldonx, Shelldony)
        Shelldon.st()

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Game Over", font=font_setup)
        timer_up = True
        manage_leaderboard()
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval) 
 

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global Shelldon

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, Shelldon, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, Shelldon, score)

#--------Score display code----------
Score_Display = trtl.Turtle(shape=turtleshape)
Score_Display.color(turtlecolor)
Score_Display.shapesize(turtlesize)
Score_Display.ht()
Score_Display.pensize(10)
 
Score_Display.penup()
Score_Display.goto(-440,350)
Score_Display.pendown()

font_setup = ("Arial", 30, "bold")
Score_Display.write(score, font = font_setup)

#-------countdown-------------
counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(-70,320)
 
#-------events----------------
wn = trtl.Screen()

wn.ontimer(countdown, counter_interval)
Shelldon.onclick(turtle_clicked)
 
wn.mainloop()

