user_x = 1
user_y = 1
mx = 100
my = 100
new_number = 0
gap = False

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
        if vertical_line_x_axis != 150 and vertical_line_x_axis != 300:
            pygame.draw.line(screen, (0, 0, 0), (vertical_line_x_axis, 50), (vertical_line_x_axis, 500)) 
        vertical_line_count += 1
        vertical_line_x_axis += 50

def bold_vertical_gridline():
    bold_vertical_line_count = 0
    bold_vertical_line_x_axis = 150
    while bold_vertical_line_count < 2:
        pygame.draw.line(screen, (0, 0, 255), (bold_vertical_line_x_axis, 50), (bold_vertical_line_x_axis, 500)) 
        bold_vertical_line_count += 1
        bold_vertical_line_x_axis += 150

def horizontal_gridline():
    horizontal_line_count = 0
    horizontal_line_y_axis = 50
    while horizontal_line_count < 9:
        if horizontal_line_y_axis != 200 and horizontal_line_y_axis != 350:
            pygame.draw.line(screen, (0, 0, 0), (0, horizontal_line_y_axis), (450, horizontal_line_y_axis)) 
        horizontal_line_count += 1
        horizontal_line_y_axis += 50

def bold_horizontal_gridline():
    bold_horizontal_line_count = 0
    bold_horizontal_line_y_axis = 200
    while bold_horizontal_line_count < 2:
        pygame.draw.line(screen, (0, 0, 255), (0, bold_horizontal_line_y_axis), (450, bold_horizontal_line_y_axis)) 
        bold_horizontal_line_count += 1
        bold_horizontal_line_y_axis += 150

#fonts
font = pygame.font.Font('freesansbold.ttf', 30)
big_font = pygame.font.Font('freesansbold.ttf', 50)
huge_font = pygame.font.Font('freesansbold.ttf', 80)

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

#the solution
answer_row1 = [0, 0, 9, 0, 1, 7, 0, 0, 0, 2, 0]
answer_row2 = [0, 6, 2, 7, 0, 4, 0, 0, 1, 3, 0]
answer_row3 = [0, 1, 4, 8, 3, 0, 2, 7, 0, 0, 0]

answer_row4 = [0, 3, 7, 0, 0, 0, 8, 1, 0, 0, 0]
answer_row5 = [0, 0, 5, 2, 0, 1, 0, 9, 6, 0, 0]
answer_row6 = [0, 0, 0, 6, 4, 0, 0, 0, 7, 8, 0]

answer_row7 = [0, 0, 0, 5, 9, 0, 4, 2, 8, 1, 0]
answer_row8 = [0, 4, 8, 0, 0, 3, 0, 6, 5, 9, 0]
answer_row9 = [0, 2, 0, 0, 0, 8, 1, 0, 3, 0, 0]


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
            number = font.render(str(eval(internal_index)), True, (255, 255, 255))
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
                    should_update_number = True
                elif event.key == pygame.K_2:
                    new_number = 2
                    selecting = False
                    should_update_number = True
                elif event.key == pygame.K_3:
                    new_number = 3
                    selecting = False
                    should_update_number = True
                elif event.key == pygame.K_4:
                    new_number = 4
                    selecting = False
                    should_update_number = True
                elif event.key == pygame.K_5:
                    new_number = 5
                    selecting = False
                    should_update_number = True
                elif event.key == pygame.K_6:
                    new_number = 6
                    selecting = False
                    should_update_number = True
                elif event.key == pygame.K_7:
                    new_number = 7
                    selecting = False
                    should_update_number = True
                elif event.key == pygame.K_8:
                    new_number = 8
                    selecting = False
                    should_update_number = True
                elif event.key == pygame.K_9:
                    new_number = 9
                    selecting = False
                    should_update_number = True
                elif event.key == pygame.K_0:
                    new_number = 0
                    selecting = False
                    should_update_number = True
                elif event.key == pygame.K_ESCAPE:
                    selecting = False
                elif event.key == pygame.K_SPACE:
                    selecting = False


def updating_numbers():
    global should_update_number
    if should_update_number == True:
        user_x = math.ceil(mx / 50)
        user_y = math.ceil((my - 50)/ 50)

        update = "user_row" + str(user_y) + "[" + str(user_x) + "] = " + str(new_number)
        exec(update)
        should_update_number = False

def check_answer_text():
    check = font.render('''Check answer''' , True, (0, 0, 0))
    screen.blit(check, (230, 10))

def checking_solution():
    if user_row1 == answer_row1 and user_row2 == answer_row2 and user_row3 == answer_row3 and user_row4 == answer_row4\
        and user_row5 == answer_row5 and user_row6 == answer_row6 and user_row7 == answer_row7 and \
            user_row8 == answer_row8 and user_row9 == answer_row9:
            return 1
    else:
        return 0


#big functions
def main_menu():
    global title_screen
    global game_selection

    title = huge_font.render('''Sudoku!''' , True, (0, 0, 0))
    screen.blit(title, (56, 130))

    start_game = big_font.render('''Start''' , True, (0, 0, 0))
    screen.blit(start_game, (165, 228))

    credit = font.render('''Made by Josh Zhang''' , True, (0, 0, 0))
    screen.blit(credit, (67, 354))


def game_on():
    global game_selection
    global actual_game

    vertical_gridline()
    horizontal_gridline()
    bold_vertical_gridline()
    bold_horizontal_gridline()
    check_answer_text()
    display_numbers()
    display_user_numbers()
    updating_numbers()
    
    #back button
    back = font.render("Back" , True, (0, 0, 0))
    screen.blit(back, (10, 10))


def game_selector():
    global title_screen
    global game_selection
    global actual_game

    back = font.render("Back" , True, (0, 0, 0))
    screen.blit(back, (20, 450))

    game_1 = big_font.render("1" , True, (0, 0, 0))
    screen.blit(game_1 , (20, 20))
    

complete = big_font.render("Complete" , True, (0, 0, 0))
not_quite = big_font.render("Not quite..." , True, (0, 0, 0))
def check_answer():
    global display_status
    global actual_game
    display_status = True
    actual_game = False


#game display function control
title_screen = True
game_selection = False
actual_game = False
display_status = False

running = True
while running:

    screen.fill((252, 169, 3)) #252, 169, 3

    if title_screen == True:
        main_menu()

    if game_selection == True:
        game_selector()

    if actual_game == True:
        game_on()
    
    if display_status == True:
        if checking_solution() == 1:
            screen.blit(complete, (200, 200))
        elif checking_solution() == 0:
            screen.blit(not_quite, (200, 200))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            print (mx, my)
            gap = False

            #display status
            if display_status == True and gap == False:
                display_status = False
                actual_game = True
                gap = True

            #actual game
            if actual_game == True and display_status == False and gap == False:
                if my > 50:
                    user_selection()
                    gap = True

                if my < 50 and mx > 225:
                    check_answer()
                    gap = True

            if actual_game == True and mx < 86 and my < 39 and gap == False:
                game_selection = True
                actual_game = False
                gap = True

            #title screen
            if title_screen == True and gap == False and mx > 165 and mx < 286 and my > 232 and my < 275:
                title_screen = False
                game_selection = True
                gap = True

            #game selection
            if game_selection == True and gap == False:
                
                #back button
                if mx > 16 and mx < 102 and my > 445 and my < 481:
                    game_selection = False
                    title_screen = True
                    gap = True

                #stage selection
                if mx > 14 and mx < 52 and my > 20 and my < 66:
                    game_selection = False
                    actual_game = True
                    gap = True


    pygame.display.update()
