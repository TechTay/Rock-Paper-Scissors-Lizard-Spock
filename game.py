import random
from time import sleep
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
        self.match_startup()
               


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

                
    def match_startup(self):
        
        user_action = True
        while True:
            user_action = input("Enter a choice (Rock, Paper, Scissors, Lizard, Spock): ")
            possible_actions = ["Rock", "Paper", "Scissors","Lizard","Spock"]
            computer_action = random.choice(possible_actions)
            print(f"\n You chose {user_action}'\n' computer chose {computer_action}.'\n' ")

            if user_action == computer_action:
                print(f"Both players selected {user_action}. It's a tie!")
            
            elif user_action == "rock":
                if computer_action == "scissors":
                    print("You win!"'\n')
                else:
                    print("You lose."'\n')

            elif user_action == "paper":
                if computer_action == "rock":
                    print("You win!"'\n')
                else:
                    print("You lose."'\n')

            elif user_action == "scissors":
                if computer_action == "paper":
                    print("You win!"'\n')
                else:
                    print("You lose."'\n')

            elif user_action == 'Spock':
                if computer_action == 'Rock':
                    print('You win!''\n')
                else:
                    print('You lose!''\n')

            elif user_action == "Lizard":
                if computer_action == "Paper":
                    print("You win!"'\n')
                else:
                    print('You Lose!''\n')

            elif user_action == "Rock":
                if computer_action == "Lizard":
                    print("You win!"'\n')
                else:
                    print('You Lose!''\n')

            elif user_action == "Lizard":
                if computer_action == "Spock":
                    print("You win!"'\n')
                else:
                    print('You Lose!''\n')

            elif user_action == "Spock":
                if computer_action == "Scissors":
                    print("You win!"'\n')
                else:
                    print('You Lose!''\n')

            elif user_action == "Scissors":
                if computer_action == "Lizard":
                    print("You win!"'\n')
                else:
                    print('You Lose!''\n')

            elif user_action == "Paper":
                if computer_action == "Spock":
                    print("Lizard eats paper! You win!"'\n')
                else:
                    print('Rock crushes Lizard. You Lose!''\n')
            
                if user_action == '2':
                    print(f'{self.player_one} won best out of 3 games!')
            elif computer_action == '2':
                    print(f'{self.Player_two} won best of 3 games!')
                    
                    play_again = input("Play again? (y/n): "'\n')
                    if play_again.lower() != "y":
                        break

    