from os import name
import random
from time import sleep
from player import Player
from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.create_game()
        self.player_one = Human('Player One')
        self.Player_two = AI(name)
        

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
                return Human('Player Two')
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
            
            elif user_action == "Rock":
                self.player_one.score += 1
                if computer_action == "Scissors":
                    print("You win!"'\n')
                else:
                    self.Player_two.score += 1
                    print("You lose."'\n')
                
            elif user_action == "paper":
                self.player_one.score += 1
                if computer_action == "rock":
                    self.Player_two.score += 1
                    print("You win!"'\n')
                else:
                    print("You lose."'\n')
                
            elif user_action == "scissors":
                self.player_one.score += 1
                if computer_action == "paper":
                    self.Player_two.score += 1
                    print("You win!"'\n')
                else:
                    print("You lose."'\n')
                
            elif user_action == 'Spock':
                self.player_one.score += 1
                if computer_action == 'Rock':
                    self.Player_two.score += 1   
                    print('You win!''\n')
                else:
                    print('You lose!''\n')

            elif user_action == "Lizard":
                self.player_one.score += 1
                if computer_action == "Paper":
                    self.Player_two.score += 1
                    print("You win!"'\n')
                else:
                    print('You Lose!''\n')

            elif user_action == "Rock":
                self.player_one.score += 1
                if computer_action == "Lizard":
                    self.Player_two.score += 1
                    print("You win!"'\n')
                else:
                    print('You Lose!''\n')

            elif user_action == "Lizard":
                self.player_one.score += 1
                if computer_action == "Spock":
                    self.Player_two.score += 1
                    print("You win!"'\n')
                else:
                    print('You Lose!''\n')

            elif user_action == "Spock":
                self.player_one.score += 1
                if computer_action == "Scissors":
                    self.Player_two.score += 1
                    print("You win!"'\n')
                else:
                    print('You Lose!''\n')

            elif user_action == "Scissors":
                self.player_one.score += 1
                if computer_action == "Lizard":
                    self.Player_two.score += 1
                    print("You win!"'\n')
                else:
                    print('You Lose!''\n')

            elif user_action == "Paper":
                self.player_one.score += 1
                if computer_action == "Spock":
                    self.Player_two.score += 1
                    print("You win!"'\n')
                else:
                    print('You Lose!''\n')
                    
            if self.player_one.score == 2:
                return self.display_winner()
            elif self.Player_two.score == 2:
                return self.display_winner()

            # play_again = input("Play again? (y/n): "'\n')
            # if play_again.lower() != "y":
            #     break

    def display_winner(self):
        while self.player_one.score or self.Player_two.score:
            if self.player_one.score == 2:
                print(f'Player One wins!')

            else:
                print(f'{self.Player_two} wins!')

            play_again = input("Play again? (y/n): "'\n')
            if play_again.lower() != "y":
                break