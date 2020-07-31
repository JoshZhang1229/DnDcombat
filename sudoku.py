'''
2020/07/24
The end goal is to make it easy to add more puzzles

'''
user_x = 1
user_y = 1
mx = 100
my = 100
new_number = 0

import math

import pygame

pygame.init()

screen = pygame.display.set_mode((450,500)) #50*9

pygame.display.set_caption("Sudoku")

#gridlines
def vertical_gridline():
    vertical_line_count = 0
    vertical_line_x_axis = 50
    while vertical_line_count < 8:
        pygame.draw.line(screen, (0, 0, 0), (vertical_line_x_axis, 50), (vertical_line_x_axis, 500)) 
        vertical_line_count += 1
        vertical_line_x_axis += 50

def horizontal_gridline():
    horizontal_line_count = 0
    horizontal_line_x_axis = 50
    while horizontal_line_count < 9:
        pygame.draw.line(screen, (0, 0, 0), (0, horizontal_line_x_axis), (450, horizontal_line_x_axis)) 
        horizontal_line_count += 1
        horizontal_line_x_axis += 50

#font
font = pygame.font.Font('freesansbold.ttf', 30)

#the numbers
row1 = [0, 5, 0, 3, 0, 0, 6, 8, 4, 0, 0]
row2 = [0, 0, 0, 0, 8, 0, 9, 5, 0, 0, 0]
row3 = [0, 0, 0, 0, 0, 5, 0, 0, 9, 6, 0]
row4 = [0, 0, 0, 4, 6, 9, 0, 0, 2, 5, 0]
row5 = [0, 8, 0, 0, 7, 0, 3, 0, 0, 4, 0]
row6 = [0, 9, 1, 0, 0, 2, 5, 3, 0, 0, 0]
row7 = [0, 7, 3, 0, 0, 6, 0, 0, 0, 0, 0]
row8 = [0, 0, 0, 1, 2, 0, 7, 0, 0, 0, 0]
row9 = [0, 0, 6, 9, 5, 0, 0, 4, 0, 7, 0]

#user inputed numbers
user_row1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
user_row2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
user_row3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
user_row4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
user_row5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
user_row6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
user_row7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
user_row8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
user_row9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#17, 65 should be the starting point of box 1,1
#displaying the numbers
def display_numbers():
    box_index = 11
    while box_index <= 99:
        horizontal_index = box_index % 10
        vertical_index = math.floor(box_index / 10)

        internal_index = "row" + str(vertical_index) + "[" + str(horizontal_index) + "]"

        if eval(internal_index) != 0:
            number = font.render(str(eval(internal_index)), True, (0, 0, 0))
            box_print = screen.blit(number, (-33 + 50 * horizontal_index, 15 + 50 * vertical_index))    

        box_index += 1

def display_user_numbers():
    box_index = 11
    while box_index <= 99:
        horizontal_index = box_index % 10
        vertical_index = math.floor(box_index / 10)

        internal_index = "user_row" + str(vertical_index) + "[" + str(horizontal_index) + "]"

        if eval(internal_index) != 0:
            number = font.render(str(eval(internal_index)), True, (0, 0, 0))
            box_print = screen.blit(number, (-33 + 50 * horizontal_index, 15 + 50 * vertical_index))    

        box_index += 1

def user_selection():
    user_x = math.ceil(mx / 50)
    user_y = math.ceil((my - 50) / 50)

    internal_index = "row" + str(user_y) + "[" + str(user_x) + "]"

    if eval(internal_index) == 0:
        print ("blank spot")
        user_answering()

should_update_number = False
def user_answering():
    selecting = True

    while selecting:
        global new_number
        global should_update_number
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    new_number = 1
                    selecting = False
                elif event.key == pygame.K_2:
                    new_number = 2
                    selecting = False
                elif event.key == pygame.K_3:
                    new_number = 3
                    selecting = False
                elif event.key == pygame.K_4:
                    new_number = 4
                    selecting = False
                elif event.key == pygame.K_5:
                    new_number = 5
                    selecting = False
                elif event.key == pygame.K_6:
                    new_number = 6
                    selecting = False
                elif event.key == pygame.K_7:
                    new_number = 7
                    selecting = False
                elif event.key == pygame.K_8:
                    new_number = 8
                    selecting = False
                elif event.key == pygame.K_9:
                    new_number = 9
                    selecting = False
                elif event.key == pygame.K_ESCAPE:
                    selecting = False
                elif event.key == pygame.K_SPACE:
                    selecting = False
    
    if selecting == False:
        should_update_number = True


def updating_numbers():
    global should_update_number
    if should_update_number == True:
        user_x = math.ceil(mx / 50)
        user_y = math.ceil((my - 50)/ 50)

        update = "user_row" + str(user_y) + "[" + str(user_x) + "] = " + str(new_number)
        exec(update)
        should_update_number = False

def main_menu():
    title = font.render('''Sudoku!''' , True, (0, 0, 0))
    screen.blit(title, (165, 10))

running = True
while running:

    screen.fill((252,169,3))

    vertical_gridline()
    horizontal_gridline()
    main_menu()
    display_numbers()
    display_user_numbers()
    updating_numbers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            print (mx, my)
            if my > 50:
                user_selection()


    pygame.display.update()
