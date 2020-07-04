import pygame
import time
import sys

pygame.init()

DISPLAY_WIDTH = 1800
DISPLAY_HEIGHT = 500

FPS = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (32, 32, 32)
GREY_CLICK = (96, 96, 96)

WHITE_KEYS = ["C2", "D2", "E2", "F2", "G2", "A2", "B2", "C3", "D3", "E3", "F3", "G3", "A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5", "A5", "B5"]
BLACK_KEYS = ["C#2", "D#2", "F#2", "G#2", "A#2", "C#3", "D#3", "F#3", "G#3", "A#3", "C#4", "D#4", "F#4", "G#4", "A#4", "C#5", "D#5", "F#5", "G#5", "A#5"]

FONT = 'URW Chancery L, Medium Itallic' 
WHITE_KEY_FONT_SIZE = 40
BLACK_KEY_FONT_SIZE = 30
WHITE_KEYS_TEXT_RANGE = [70, 130, 190, 250, 310, 370, 430, 490, 550, 610, 670, 730, 790, 850, 910, 970, 1030, 1090, 1150, 1210, 1270, 1330, 1390, 1450, 1510, 1570, 1630, 1690]

WHITE_X_COORDINATES = [55, 115, 175, 235, 295, 355, 415, 475, 535, 595, 655, 715, 775, 835, 895, 955, 1015, 1075, 1135, 1195, 1255, 1315, 1375, 1435, 1495, 1555, 1615, 1675, 1735] 
WHITE_SOUNDS = {'C2' : 'music/C2.ogg', 'D2' : 'music/D2.ogg', 'E2' : 'music/E2.ogg', 'F2' : 'music/F2.ogg', 'G2' : 'music/G2.ogg', 'A2' : 'music/A2.ogg', 'B2' : 'music/B2.ogg', 'C3' : 'music/C3.ogg', 'D3' : 'music/D3.ogg', 'E3' : 'music/E3.ogg', 'F3' : 'music/F3.ogg', 'G3' : 'music/G3.ogg', 'A3' : 'music/A3.ogg', 'B3' : 'music/B3.ogg', 'C4' : 'music/C4.ogg', 'D4' : 'music/D4.ogg', 'E4' : 'music/E4.ogg', 'F4' : 'music/F4.ogg', 'G4' : 'music/G4.ogg', 'A4' : 'music/A4.ogg', 'B4' : 'music/B4.ogg', 'C5' : 'music/C5.ogg', 'D5' : 'music/D5.ogg', 'E5' : 'music/E5.ogg', 'F5' : 'music/F5.ogg', 'G5' : 'music/G5.ogg', 'A5' : 'music/A5.ogg', 'B5' : 'music/B5.ogg' }

BLACK_X_COORDINATES = [90, 150, 270, 330, 390, 510, 570, 690, 750, 810, 930, 990, 1110, 1170, 1230, 1350, 1410, 1530, 1590, 1650]
BLACK_SOUNDS = {'C#2' : 'music/C#2.ogg', 'D#2' : 'music/D#2.ogg', 'F#2' : 'music/F#2.ogg', 'G#2' : 'music/G#2.ogg', 'A#2' : 'music/A#2.ogg', 'C#3' : 'music/C#3.ogg', 'D#3' : 'music/D#3.ogg', 'F#3' : 'music/F#3.ogg', 'G#3' : 'music/G#3.ogg', 'A#3' : 'music/A#3.ogg', 'C#4' : 'music/C#4.ogg', 'D#4' : 'music/D#4.ogg', 'F#4' : 'music/F#4.ogg', 'G#4' : 'music/G#4.ogg', 'A#4' : 'music/A#4.ogg', 'C#5' : 'music/C#5.ogg', 'D#5' : 'music/D#5.ogg', 'F#5' : 'music/F#5.ogg', 'G#5' : 'music/G#5.ogg', 'A#5' : 'music/A#5.ogg'}

screen  = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('PyPiano')

def key_display(font, font_size, note, text_colour, coordinates):
    font = pygame.font.SysFont(font, font_size)
    text = font.render(note, True, text_colour)
    screen.blit(text, coordinates)

def keys_white(x):
    return pygame.Rect(x, 250, 55, 220)

def keys_black(x):
    return pygame.Rect(x, 70, 45, 180)

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
    screen.fill(GREY)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for pixel in range(55, 1735, 60):
        pygame.draw.rect(screen, WHITE, [pixel, 250, 55, 220])
    
    pygame.draw.rect(screen, BLACK, [90, 70, 45, 180])
    pygame.draw.rect(screen, BLACK, [150, 70, 45, 180])
    
    for pixel in range(270, 450, 60):
        pygame.draw.rect(screen, BLACK, [pixel, 70, 45, 180])

    pygame.draw.rect(screen, BLACK, [510, 70, 45, 180])
    pygame.draw.rect(screen, BLACK, [570, 70, 45, 180])
    

    for pixel in range(690, 870, 60):
        pygame.draw.rect(screen, BLACK, [pixel, 70, 45, 180])

    pygame.draw.rect(screen, BLACK, [930, 70, 45, 180])
    pygame.draw.rect(screen, BLACK, [990, 70, 45, 180])

    for pixel in range(1110, 1290, 60):
        pygame.draw.rect(screen, BLACK, [pixel, 70, 45, 180])

    pygame.draw.rect(screen, BLACK, [1350, 70, 45, 180])
    pygame.draw.rect(screen, BLACK, [1410, 70, 45, 180])

    for pixel in range(1530, 1710, 60):
        pygame.draw.rect(screen, BLACK, [pixel, 70, 45, 180])
    
    key_display(FONT, BLACK_KEY_FONT_SIZE, "C#2", WHITE, (93,100))
    key_display(FONT, BLACK_KEY_FONT_SIZE, "D#2", WHITE, (155,100))

    key_display(FONT, BLACK_KEY_FONT_SIZE, "F#2", WHITE, (275,100))
    key_display(FONT, BLACK_KEY_FONT_SIZE, "G#2", WHITE, (333,100))
    key_display(FONT, BLACK_KEY_FONT_SIZE, "A#2", WHITE, (393,100))

    key_display(FONT, BLACK_KEY_FONT_SIZE, "C#3", WHITE, (514,100))
    key_display(FONT, BLACK_KEY_FONT_SIZE, "D#3", WHITE, (575,100))

    key_display(FONT, BLACK_KEY_FONT_SIZE, "F#3", WHITE, (696,100))
    key_display(FONT, BLACK_KEY_FONT_SIZE, "G#3", WHITE, (754,100))
    key_display(FONT, BLACK_KEY_FONT_SIZE, "A#3", WHITE, (814,100))

    key_display(FONT, BLACK_KEY_FONT_SIZE, "C#4", WHITE, (935,100))
    key_display(FONT, BLACK_KEY_FONT_SIZE, "D#4", WHITE, (994,100))

    key_display(FONT, BLACK_KEY_FONT_SIZE, "F#4", WHITE, (1114,100))
    key_display(FONT, BLACK_KEY_FONT_SIZE, "G#4", WHITE, (1174,100))
    key_display(FONT, BLACK_KEY_FONT_SIZE, "A#4", WHITE, (1234,100))

    key_display(FONT, BLACK_KEY_FONT_SIZE, "C#5", WHITE, (1354,100))
    key_display(FONT, BLACK_KEY_FONT_SIZE, "D#5", WHITE, (1414,100))
    
    key_display(FONT, BLACK_KEY_FONT_SIZE, "F#5", WHITE, (1534,100))
    key_display(FONT, BLACK_KEY_FONT_SIZE, "G#5", WHITE, (1594,100))
    key_display(FONT, BLACK_KEY_FONT_SIZE, "A#5", WHITE, (1654,100))

    for key in range(len(WHITE_KEYS)):
        key_display(FONT, WHITE_KEY_FONT_SIZE, WHITE_KEYS[key], BLACK, (WHITE_KEYS_TEXT_RANGE[key], 400))
        
    pygame.display.update()
    pygame.display.flip()

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for x in range(len(WHITE_X_COORDINATES)):
        if keys_white(WHITE_X_COORDINATES[x]).collidepoint(mouse) and click[0]:
            pygame.mixer.Sound.play(pygame.mixer.Sound(WHITE_SOUNDS[WHITE_KEYS[x]]))
            pygame.draw.rect(screen, GREY_CLICK, keys_white(WHITE_X_COORDINATES[x]))
            pygame.display.update()
            pygame.display.flip()
            pygame.time.delay(500)
            pygame.draw.rect(screen, WHITE, keys_white(WHITE_X_COORDINATES[x]))

    for x in range(len(BLACK_X_COORDINATES)):
        if keys_black(BLACK_X_COORDINATES[x]).collidepoint(mouse) and click[0]:
            pygame.mixer.Sound.play(pygame.mixer.Sound(BLACK_SOUNDS[BLACK_KEYS[x]]))
            pygame.draw.rect(screen, GREY_CLICK, keys_black(BLACK_X_COORDINATES[x]))
            pygame.display.update()
            pygame.display.flip()
            pygame.time.delay(200)
            pygame.draw.rect(screen, BLACK, keys_black(BLACK_X_COORDINATES[x]))


