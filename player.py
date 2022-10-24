# Parent Class

from ai import AI
from human import Human

class Player:
    def __init__(self, name):
        self.name = name
        self.rspls_list = ['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard']