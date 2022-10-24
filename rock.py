from rspls_selection import RSPLS_Selection

# strong against Lizard and scissors, weak against paper and Spock

class Rock(RSPLS_Selection):
    def __init__(self):
        super().__init__('Rock', 1)
        pass

    def attack(self, opponent):
        if opponent.name == 'Paper' or opponent.name == 'Spock':
            opponent.health_points -= self.attack_power * .5

        elif opponent.name == 'Lizard' or opponent.name == 'Scissors':
            opponent.health_points -= self.attack_power * 2
        else:
            print(f'You both selected the same option! Please choose again.')