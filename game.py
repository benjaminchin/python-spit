from card import *
from settings import *
from spritesheet import Spritesheet
import random
import sys 
import pygame as pg
from pygame.locals import *

def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    canvas = pg.Surface((WIDTH, HEIGHT))


    #  x, y = pg.mouse.get_pos()

    all_sprites = pg.sprite.Group()

    screen.fill(BLACK)
    canvas.fill(BLACK)
    pg.display.set_caption(TITLE)
    clock = pg.time.Clock()
    running = True

    deck = []
    for i in range(13):
        deck.append(Card(i+1, 'h'))
        deck.append(Card(i+1, 'd'))
        deck.append(Card(i+1, 's'))
        deck.append(Card(i+1, 'c'))
   
    random.shuffle(deck)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                """for card in deck[0:5]:
                    if card.sprite.get_rect().collidepoint(x, y):
                        print('collision!')"""
                print(x, y)
        
        screen.fill(GREEN)
        canvas.fill(GREEN)

        for i in range(5):
            canvas.blit(deck[i].sprite, ((i+1)*125 - CARD_WIDTH/2, HEIGHT/2 - CARD_HEIGHT/2))

        screen.blit(canvas, (0, 0))
        pg.display.update()

if __name__ == '__main__':
    main()
