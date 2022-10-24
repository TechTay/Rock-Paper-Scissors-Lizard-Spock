from rspls_selection import RSPLS_Selection

# strong against Scissors and Rock, weak against Paper and Lizard

class Rock(RSPLS_Selection):
    def __init__(self):
        super().__init__('Spock', 1)
        pass

    def attack(self, opponent):
        pass