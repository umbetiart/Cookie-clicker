import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
brown = (255, 0, 0)
blue = (50, 153, 213)
 
snak_width = 600
snak_height = 400
 
snak = pygame.display.set_mode((snak_width, snak_height))
pygame.display.set_caption('SNAKE GAME FOR ADDITIONAL COOKIES')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("Times New Roman", 25)
score_font = pygame.font.SysFont("Calibri", 35)
 
 
def Your_score(score):
    value = score_font.render("COOKIES GOT: " + str(score), True, yellow)
    snak.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(snak, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    snak.blit(mesg, [snak_width / 6, snak_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = snak_width / 2
    y1 = snak_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    food_axis = round(random.randrange(0, snak_width - snake_block) / 10.0) * 10.0
    food_y_axis = round(random.randrange(0, snak_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            snak.fill(white)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= snak_width or x1 < 0 or y1 >= snak_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        snak.fill(white)
        pygame.draw.rect(snak, brown, [food_axis, food_y_axis, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == food_axis and y1 == food_y_axis:
            food_axis = round(random.randrange(0, snak_width - snake_block) / 10.0) * 10.0
            food_y_axis = round(random.randrange(0, snak_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
