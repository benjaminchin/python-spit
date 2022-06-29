from settings import *
from spritesheet import *

class Card:

    def __init__(self, rank, suit):
        self.rank = rank #  1-13
        self.suit = suit #  h, d, s, c 
        self.color = 'r'
        
        if self.suit == 's' or self.suit == 'c':
            self.color = 'b'

        #  sprite coordinates
        suits = {'h' : CARD_HEIGHT * 2, 'd' : CARD_HEIGHT * 3, 's' : CARD_HEIGHT, 'c' : 0}
        self.y = suits[suit]
        self.x = (rank - 1) * CARD_WIDTH

        spritesheet = Spritesheet(FILENAME)
        self.sprite = spritesheet.get_sprite(self.x, self.y, CARD_WIDTH, CARD_HEIGHT)
