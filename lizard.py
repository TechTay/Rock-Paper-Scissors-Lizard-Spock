from rspls_selection import RSPLS_Selection

# strong against Spock and Paper, weak against Rock and Scissors

class Rock(RSPLS_Selection):
    def __init__(self):
        super().__init__('Lizard', 1)
        pass

    def attack(self, opponent):
        if opponent.name == 'Rock' or opponent.name == 'Scissors':
            opponent.health_points -= self.attack_power * .5
        elif opponent.name == 'Spock' or opponent.name == 'Paper':
            opponent.health_points -= self.attack_power * 2
        else:
            print(f'You both selected the same option! Please choose again.')