from rspls_selection import RSPLS_Selection

# strong against Spock and Paper, weak against Rock and Scissors

class Rock(RSPLS_Selection):
    def __init__(self):
        super().__init__('Lizard', 1)
        pass

    def attack(self, opponent):
        pass