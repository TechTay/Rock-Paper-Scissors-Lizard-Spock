from unicodedata import name
from player import Player
from human import Human
from ai import AI


class Game:
    def __init__(self):
        pass

    def run_game(self):
        self.welcome()
        user_input = input(f'''
        
                    Hit "Enter" on the keyboard to start!
                    
                    ''')

        print(user_input)

        self.game_info()
        


    def welcome(self):
        print('''
        
                Welcome to Rock, Paper, Scissors, Lizard, Spock.''' '\n'
                
                )

    def game_info(self):
        
        print('Each match will be the best of three games!')
        print('You will use the number keys to choose your gesture.' '\n')
        

        print('Scissors cut Paper' '\n' 'Paper covers Rock' '\n' 'Rock crushes Lizard' '\n' 'Lizard Poisons Spock' '\n' 'Spock smashes Scissors' '\n' 'Scissors decapitates Lizard' '\n' 'Lizard eats Paper' '\n' 'Paper disproves Spock' '\n' 'Spock vaporizes Rock' '\n' 'Rock crushes Scissors''\n')


    def number_of_players(self):
        con_bool = input(f'How many players? 1 or 2' '\n')
        while con_bool:
            if con_bool == '1':
                print('Great! You chose one player mode.''\n')
                break
            elif con_bool == '2':
                print('Great! You chose multiplayer mode.''\n')
                break
            else:
                print('Invalid selection, please choose option "1" or "2".''\n')
                return self.number_of_players()
                
    def name_to_number(self, name):
        bool2 = input(f'Choose 0 for Rock''\n''Choose 1 for Spock''\n''Choose 2 for Paper''\n''Choose 3 for Lizard''\n''Choose 4 for Scissors''\n' )
        while bool2:

            if(name == 'Rock'):
                return 0;
            elif(name == 'Spock'):
                return 1;
            elif(name == 'Paper'):
                return 2;
            elif(name == 'Lizard'):
                return 3;
            elif(name == 'Scissors'):
                return 4;
            else:
                print("Invalid input. Please try again.")
                return name.name_to_number()

    def rpsls(player_choice):
        print("\n")
        print('Player chooses' +)