import pygame
import os
import math
from bitboard import Bitboard

white = "#eeeed2"
green = "#769656"

def load_icons():
    global white_pawn, white_knight, white_bishop, white_rook, white_queen, white_king, black_pawn, black_knight, black_bishop, black_rook, black_queen, black_king
    white_pawn = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "white_pawn.png")))
    white_knight = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "white_knight.png")))
    white_bishop = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "white_bishop.png")))
    white_rook = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "white_rook.png")))
    white_queen = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "white_queen.png")))
    white_king = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "white_king.png")))
    black_pawn = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "white_pawn.png")))
    black_knight = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "white_knight.png")))
    black_bishop = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "white_bishop.png")))
    black_rook = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "white_rook.png")))
    black_queen = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "white_queen.png")))
    black_king = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "white_king.png")))

def display_position(position: list[int]):
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    clock = pygame.time.Clock()
    # render game here
    
    #IF I SEE BLUE SOMETHING IS TERRIBLY MESSED UP
    screen.fill(("blue"))

    #CHECKER BOARD
    for x in range(0,8):
        for y in range(0,8):
                if ((x+y) % 2) == 0:
                    pygame.draw.rect(screen, white, pygame.Rect(x*100,y*100,100,100))
                else:
                    pygame.draw.rect(screen, green, pygame.Rect(x*100,y*100,100,100))
    
    load_icons()
    for x in range(12):
        #finding what squares are occupied
        found = []
        for y in range(64):
            checker = 2**y
            if (checker & x) > 0:
                found.append(y)
        match x:
            case 0:
                for z in found:
                    #starting at a1
                    screen.blit(white_pawn, (-13+(z%8)*100, 690+math.floor(z/8)))
                   
         
    #screen.blit(white_pawn, (-13, -10))
    ##top right centered white pawn
    #screen.blit(white_pawn, (-13+(z%8)*100, 690+math.floor(z/8)))
    ##formula to plot on right location on board

    pygame.display.flip()

    clock.tick(60)

    pygame.quit()