from rspls_selection import RSPLS_Selection

# strong against Rock and Spock, weak against Scissors and Lizard

class Rock(RSPLS_Selection):
    def __init__(self):
        super().__init__('Paper', 1)
        pass

    def attack(self, opponent):
        pass