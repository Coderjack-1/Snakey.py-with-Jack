author = 'Harsh Poriya'

#Importing The Modules
import pygame
import random
import os

#Initialization
pygame.mixer.init()
pygame.init()

#Creating The window
screen_width = 1000
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
snakegreen = (35, 45, 40)
green = (0,255,0)
blue = (0,162,255)

#Game Backgrounds
bg1 = pygame.image.load("screen/first.jpg")
bg1 = pygame.transform.scale(bg1, (screen_width, screen_height)).convert_alpha()
bg2 = pygame.image.load("screen/background_2.jpg")
bg2 = pygame.transform.scale(bg2, (screen_width, screen_height)).convert_alpha()
bg3 = pygame.image.load("screen/last_1.jpg")
bg3 = pygame.transform.scale(bg3, (screen_width, screen_height)).convert_alpha()
bg4 = pygame.image.load("screen/food.jpg")
bg4 = pygame.transform.scale(bg4, (screen_width, screen_height)).convert_alpha()
logo = pygame.image.load("screen/logo.jpg")
food = pygame.image.load("screen/food.jpg")
#food_y = pygame.image.load("screen/food.jpg")

#Game Window

#pygame.display.set_icon(logo)
pygame.display.set_caption("SNAKEY.py BY J@CK")
pygame.display.update()

#Music
pygame.mixer.music.load('music/welcome.mp3')
pygame.mixer.music.play(100)
pygame.mixer.music.set_volume(1.0)

#Variables For The Game
clock = pygame.time.Clock()
font = pygame.font.SysFont('Rockwell', 40)

def text_screen(text, color, x, y):
   screen_text = font.render(text, True, color)
   gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snake_list, snake_size):
   for x,y in snake_list:
       pygame.draw.ellipse(gameWindow, black, [x, y, snake_size, snake_size])


#Welcome Screen

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.blit(bg1, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.fadeout(100)
                    pygame.mixer.music.load('music/middle.mp3')
                    pygame.mixer.music.play(100)
                    pygame.mixer.music.set_volume(1.0)
                    gameloop()
        pygame.display.update()
        clock.tick(60)

# Game Loop
def gameloop():

# Game specific variables
   exit_game = False
   game_over = False
   snake_x = 10
   snake_y = 10
   velocity_x = 0
   velocity_y = 0
   snake_list = []
   snake_length = 1

#Highscore Build
   if(not os.path.exists("Highscore.txt")):
       with open("Highscore.txt", "w") as f:
           f.write("0")
   with open("Highscore.txt", "r") as f:
            Highscore = f.read()

#Food
   #pygame.display.set_icon(food)
   food = pygame.display.set_mode()
   food_x = random.randint(100, screen_width / 2)
   food_y = random.randint(100, screen_height / 2)
   #gameWindow = pygame.display.set_mode(food_x,food_y)
   gameWindow.blit(food,(food_x,food_y))


#Game Variables
   score = 0
   init_velocity = 2.5
   snake_size = 20
   food_size = 15
   fps = 120
   while not exit_game:
       if game_over:
           with open("Highscore.txt", "w") as f:
               f.write(str(Highscore))

#GameOverScreen

           gameWindow.blit(bg3, (0, 0))
           text_screen("Score: " + str(score ), snakegreen, 385, 350)
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   exit_game = True
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_RETURN:
                       welcome()
       else:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   exit_game = True

               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                       velocity_x = init_velocity
                       velocity_y = 0

                   if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                       velocity_x = - init_velocity
                       velocity_y = 0

                   if event.key == pygame.K_UP or event.key == pygame.K_w:
                       velocity_y = - init_velocity
                       velocity_x = 0

                   if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                       velocity_y = init_velocity
                       velocity_x = 0

                   if event.key == pygame.K_q:
                        score +=10

                   if event.key == pygame.K_e:
                        snake_length +=5


           snake_x = snake_x + velocity_x
           snake_y = snake_y + velocity_y

           if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
               score +=10
               food_x = random.randint(100, screen_width / 2)
               food_y = random.randint(100, screen_height / 2)
               snake_length +=5
               if score>int(Highscore):
                   Highscore = score

           gameWindow.blit(bg2, (0, 0))
           text_screen("Score: " + str(score) + "  Highscore: "+str(Highscore),  snakegreen, 3, 3)
           pygame.draw.ellipse(gameWindow,red, [food_x, food_y, food_size, food_size])

           head = []
           #head.append(blue)
           head.append(snake_x)
           head.append(snake_y)
           snake_list.append(head)

           #body = []
           #body.append(snake_x)
           #body.append(snake_y)
           #snake_list.append(body)


           if len(snake_list)>snake_length:
               del snake_list[0]
           if head in snake_list[:-1]:
               game_over = True
               pygame.mixer.music.load('music/last.mp3')
               pygame.mixer.music.play(1)
               pygame.mixer.music.set_volume(1.0)

           if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
               game_over = True
               pygame.mixer.music.load('music/last.mp3')
               pygame.mixer.music.play(1)
               pygame.mixer.music.set_volume(1.0)

           plot_snake(gameWindow, black, snake_list, snake_size)
       pygame.display.update()
       clock.tick(fps)
   pygame.quit()
   quit()
welcome()

