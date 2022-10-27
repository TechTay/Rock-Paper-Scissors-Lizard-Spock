# Child Class
from time import sleep
from player import Player

class Human(Player):
    
    def __init__(self,name):
        super().__init__(name)
        self.score = 0

    def player_gesture_choice(self):
        rpsls_list = ['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard']
        user_input_gesture = str(input('Please enter a gesture'))
        self.choosen_gesture = rpsls_list[user_input_gesture]
        sleep(1)
        print(self.choosen_gesture)
        