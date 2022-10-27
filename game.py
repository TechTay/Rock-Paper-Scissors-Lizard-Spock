from os import name
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
        self.display_winner()       


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
        print('Please, choose your gesture.' '\n')
        

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
                Human('Player Two')
                
            else:
                print('Invalid selection, please choose option "1" or "2".''\n')

                
    def match_startup(self):
       
        while self.player_one.score < 3 and self.Player_two.score < 3:
            user_action = input("Enter a choice (Rock, Paper, Scissors, Lizard, Spock): ")
            possible_actions = ["Rock", "Paper", "Scissors","Lizard","Spock"]
            computer_action = random.choice(possible_actions)
            print(f"\n You chose {user_action}'\n' computer chose {computer_action}.'\n' ")

            if user_action == computer_action:
                print(f"Both players selected {user_action}. It's a tie!")
            
            elif user_action == "Rock" or user_action == "rock":
                if computer_action == "Scissors" or computer_action == "Lizard":
                    print("You win!"'\n')
                    self.player_one.score += 1
                else:
                    print("You lose."'\n')
                    self.Player_two.score += 1

            elif user_action == "paper" or user_action == "Paper":
                if computer_action == "rock" or computer_action == "Spock":
                    print("You win!"'\n')
                    self.player_one.score += 1
                else:
                    print("You lose."'\n')
                    self.Player_two.score += 1

            elif user_action == "scissors" or user_action == "Scissors":
                if computer_action == "paper" or computer_action == "Lizard":
                    print("You win!"'\n')
                    self.player_one.score += 1
                else:
                    print("You lose."'\n')
                    self.Player_two.score += 1
                
            elif user_action == 'Spock' or user_action == "spock":
                if computer_action == 'Rock' or computer_action == "Scissors":  
                    print('You win!''\n')
                    self.player_one.score += 1
                else:
                    print('You lose!''\n')
                    self.Player_two.score += 1 

            elif user_action == "Lizard" or user_action == "lizard":
                if computer_action == "Paper" or computer_action == "Spock":
                    print("You win!"'\n')
                    self.player_one.score += 1
                else:
                    print('You Lose!''\n')
                    self.Player_two.score += 1
                    
            if self.player_one.score == 2:
                return self.display_winner()
            elif self.Player_two.score == 2:
                return self.display_winner()

            else:
                print('Invalid input. Please try again.')

    def display_winner(self):
        while self.player_one.score or self.Player_two.score:
            if self.player_one.score == 2:
                print(f'Player One wins!''\n')

            else:
                print(f'{self.Player_two} wins!')

            play_again = input(" That was fun! Play again? (y/n): "'\n')
            if play_again.lower() != "y":
                break
            else:
                self.player_one.score == 0 and self.Player_two.score == 0
                return Game()