from rspls_selection import RSPLS_Selection

# strong against Paper and Lizard, weak against Rock and Spock

class Rock(RSPLS_Selection):
    def __init__(self):
        super().__init__('Scissors', 1)
        pass

    def attack(self, opponent):
        pass