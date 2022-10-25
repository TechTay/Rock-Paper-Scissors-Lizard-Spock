#  Child Class
from player import Player

class AI (Player):
    def __init__(self):
        super().__init__(AI)
        self.comp_player = 'Computer Player'