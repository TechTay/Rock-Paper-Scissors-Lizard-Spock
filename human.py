# Child Class
from time import sleep
from player import Player

class Human(Player):
    
    def __init__(self,name):
        super().__init__()
        self.name = name
        self.score = 0

    def player_gesture_choice(self):
        self.player_choice =()
        rpsls_list = ['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard']
        sleep(1)
        print(f'{self.name} has picked {rpsls_list[int(self.player_choice)]}')
        