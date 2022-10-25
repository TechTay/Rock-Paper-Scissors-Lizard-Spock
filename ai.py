#  Child Class
from player import Player
import random
from time import sleep

class AI (Player):
    def __init__(self,name):
        super().__init__()
        self.name = name
        self.score = 0

    def choose_gesture(self):
        self.chosen_gesture = str(random.randint(0,4))
        rpsls_list = ['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard']
        sleep(1)
        print(f'{self.name} has picked {rpsls_list[int(self.chosen_gesture)]}')