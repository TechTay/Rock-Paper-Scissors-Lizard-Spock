from unicodedata import name
from player import Player
from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.player_one = Human('Player One')
        self.Player_two = self.create_game()
        

    def create_game(self):
        self.welcome()
        self.game_info()
        return self.number_of_players()

    def run_game(self):
        self.name_to_number()
        


    def welcome(self):
        print('''
        
                Welcome to Rock, Paper, Scissors, Lizard, Spock.''' '\n'
                
                )
        user_input = input(f'''
        
                    Hit "Enter" on the keyboard to start!
                    
                    ''')

        print(user_input)

    def game_info(self):
        
        print('Each match will be the best of three games!')
        print('You will use the number keys to choose your gesture.' '\n')
        

        print('Scissors cut Paper' '\n' 'Paper covers Rock' '\n' 'Rock crushes Lizard' '\n' 'Lizard Poisons Spock' '\n' 'Spock smashes Scissors' '\n' 'Scissors decapitates Lizard' '\n' 'Lizard eats Paper' '\n' 'Paper disproves Spock' '\n' 'Spock vaporizes Rock' '\n' 'Rock crushes Scissors''\n')


    def number_of_players(self):
        con_bool = True
        while con_bool:
            user_input = input(f'How many players? 1 or 2' '\n')
            if user_input == '1':
                print('Great! You chose one player mode.''\n')
                con_bool = False
                return AI('Computer Player')
            elif user_input == '2':
                print('Great! You chose multiplayer mode.''\n')
                con_bool = False
                return Human('Player Two')
            else:
                print('Invalid selection, please choose option "1" or "2".''\n')

                
    def name_to_number(self):
        
        con_bool2 = True
        while con_bool2:
            user_input = input(f'Choose 0 for Rock''\n''Choose 1 for Spock''\n''Choose 2 for Paper''\n''Choose 3 for Lizard''\n''Choose 4 for Scissors''\n''\n' 'Choose your gesture from the above list.''\n')
            if(user_input == '0'):
                print(' Chose Rock.')
                break
            elif(user_input == '1'):
                print('Player One Chose Spock.')
                break
            elif(user_input == '2'):
                print('Player One Chose Paper')
                break
            elif(user_input == '3'):
                print('Player One Chose Lizard')
                break
            elif(user_input == '4'):
                print('Player One Chose Scissors')
                break
            else:
                print("Invalid input. Please try again.")
            

    def current_turn(self):
        # Do a while loop but you do not need if/else statements. Logic in the turns
        
        print("\n")
        
        pass