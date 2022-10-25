# Child Class
from time import sleep
from player import Player

class Human(Player):
    
    def __init__(self,name):
        super().__init__(name)
        self.score = 0

    def player_gesture_choice(self):
        rpsls_list = ['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard']
        user_input_number = int(input('Please enter a number'))
        self.choosen_gesture = rpsls_list[user_input_number]
        sleep(1)
        print(self.choosen_gesture)
        