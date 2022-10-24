from rspls_selection import RSPLS_Selection

# strong against Paper and Lizard, weak against Rock and Spock

class Rock(RSPLS_Selection):
    def __init__(self):
        super().__init__('Scissors', 1)
        pass

    def attack(self, opponent):
        if opponent.name == 'Rock' or opponent.name == 'Spock':
            opponent.health_points -= self.attack_power * .5
        elif opponent.name == 'Paper' or opponent.name == 'Lizard':
            opponent.health_points -= self.attack_power * 2
        else:
            print(f'You both selected the same option! Please choose again.')