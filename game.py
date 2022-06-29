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
    for card in deck:
        all_sprites.add(card.sprite)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                pass
        
        screen.fill(GREEN)
        canvas.fill(GREEN)
        
        canvas.blit(deck[0].sprite, (125 - CARD_WIDTH/2, HEIGHT/2 - CARD_HEIGHT/2)) # slot 1-5
        canvas.blit(deck[1].sprite, (250 - CARD_WIDTH/2, HEIGHT/2 - CARD_HEIGHT/2))
        canvas.blit(deck[2].sprite, (375 - CARD_WIDTH/2, HEIGHT/2 - CARD_HEIGHT/2))
        canvas.blit(deck[3].sprite, (500 - CARD_WIDTH/2, HEIGHT/2 - CARD_HEIGHT/2))
        canvas.blit(deck[4].sprite, (625 - CARD_WIDTH/2, HEIGHT/2 - CARD_HEIGHT/2))

        for card in deck[0:5]:
            if card.sprite.get_rect().collidepoint(x, y):
                print('collision!')

        screen.blit(canvas, (0, 0))
        pg.display.update()

if __name__ == '__main__':
    main()
