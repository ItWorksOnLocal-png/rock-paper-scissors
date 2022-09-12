import random
import os
import time


def cpuVsHuman():
    try:
        print("====== Human vs CPU Mode ======\n")
        player1Name = input("Player name: ")
        player2Name = 'CPU'
        os.system('cls')

        hvc_validation = True
        while hvc_validation:

            print("====== Human vs CPU Mode ======\n")

            # print('='*50)

            player1Choice = input(f"{player1Name}, make a choice (R/P/S): ")

            combinations = ['R', 'P', 'S']

            cpuChoice = random.choice(combinations)


            if player1Choice == cpuChoice: # Both players chose the same option, it's a tie
                print("\n> Draw!")
                time.sleep(4)
                os.system('cls')
                hvc_validation = True

            elif player1Choice in ['R','r'] and cpuChoice in ['S','s']: # Player 1 selected Rock, Player 2 selected Scissors, Player 1 wins
                print(f'\nCPU chose: {cpuChoice}')
                print(f'\n> {player1Name} wins! Congrats!')
                time.sleep(4)
                os.system('cls')
                hvc_validation = True

            elif player1Choice in ['R','r'] and cpuChoice in ['P','p']: # Player 1 selected Rock, Player 2 selected Paper, Player 2 wins
                print(f'\nCPU chose: {cpuChoice}')
                print(f'\n> {player2Name} wins! Congrats!')
                time.sleep(4)
                os.system('cls')
                hvc_validation = True

            elif player1Choice in ['P','p'] and cpuChoice in ['R','r']: # Player 1 selected Paper, Player 2 selected Rock, Player 1 wins
                print(f'\nCPU chose: {cpuChoice}')
                print(f'\n> {player1Name} wins! Congrats!')
                time.sleep(4)
                os.system('cls')
                hvc_validation = True

            elif player1Choice in ['P','p'] and cpuChoice in ['S','s']: # Player 1 selected Paper, Player 2 selected Scissors, Player 2 wins
                print(f'\nCPU chose: {cpuChoice}')
                print(f'\n> {player2Name} wins! Congrats!')
                time.sleep(4)
                os.system('cls')
                hvc_validation = True

            elif player1Choice in ['S','s'] and cpuChoice in ['P','p']: # Player 1 selected Scissors, Player 2 selected Paper, Player 1 wins
                print(f'\nCPU chose: {cpuChoice}')
                print(f'\n> {player1Name} wins! Congrats!')
                time.sleep(4)
                os.system('cls')
                hvc_validation = True

            elif player1Choice in ['S','s'] and cpuChoice in ['R','r']: # Player 1 selected Scissors, Player 2 selected Rock, Player 2 wins
                print(f'\nCPU chose: {cpuChoice}')
                print(f'\n> {player2Name} wins! Congrats!')
                time.sleep(4)
                os.system('cls')
                hvc_validation = True

            else:
                print('\n> Invalid choice')
                time.sleep(4)
                os.system('cls')
                hvc_validation = True

    except KeyboardInterrupt:
        print("\n\n--> EXITING <--")
        time.sleep(2)
        os.system('cls')
        quit()
    
    except ValueError:
        print("\n\n--> INVALID INPUT")
        time.sleep(2)
        os.system('cls')
        hvc_validation = True
