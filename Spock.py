from rspls_selection import RSPLS_Selection

# strong against Scissors and Rock, weak against Paper and Lizard

class Rock(RSPLS_Selection):
    def __init__(self):
        super().__init__('Spock', 1)
        pass

    def attack(self, opponent):
        if opponent.name == 'Paper' or opponent.name == 'Lizard':
            opponent.health_points -= self.attack_power * .5
        elif opponent.name == 'Rock' or opponent.name == 'Scissors':
            opponent.health_points -= self.attack_power * 2
        else:
            print(f'You both selected the same option! Please choose again.')