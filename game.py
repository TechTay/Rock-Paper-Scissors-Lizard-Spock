from player import Player




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
                print('Invalid selection, please try again''\n')
                return self.number_of_players()
                
