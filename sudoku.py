'''
2020/07/24
The end goal is to make it easy to add more puzzles

'''
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


#17, 65 should be the starting point of box 1,1



#displaying the numbers
'''
def number_display_11():
    box_index = 11
    horizontal_index = box_index % 10
    vertical_index = math.floor(box_index / 10)

    internal_index = "row" + str(vertical_index) + "[" + str(horizontal_index) + "]"

    number = font.render(str(eval(internal_index)), True, (0, 0, 0))
    box_print = screen.blit(number, (-33 + 50 * horizontal_index, 15 + 50 * vertical_index))
'''


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

def user_selection():
    user_x = math.ceil(mx / 50)
    user_y = math.ceil((my - 50) / 50)

    internal_index = "row" + str(user_y) + "[" + str(user_x) + "]"

    if eval(internal_index) == 0:
        print ("blank spot")

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            print (mx, my)

            user_selection()


    pygame.display.update()
