#  Child Class
from player import Player
import random
from time import sleep

class AI (Player):
# has a
    def __init__(self,name):
        super().__init__(name)
        self.score = 0
#  does a
    def player_gesture_choice(self):
        self.chosen_gesture = str(random.randrange(0,4))
        rpsls_list = ['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard']
        sleep(1)
        print(f'{self.name} has picked {rpsls_list[str(self.chosen_gesture)]}')