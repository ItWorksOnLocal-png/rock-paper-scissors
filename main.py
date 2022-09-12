import random
import os
from click import pause
import time
# from humanVsHuman import humanVsHuman
# from cpuVsHuman import cpuVsHuman

# ===============================================================================================================================================================================


def cpuVsHuman(): # CPU vs Human game mode
    try:
        print("====== Human vs CPU Mode ======\n")
        player1Name = input("Player name: ")
        player2Name = 'CPU'
        player1_score = 0
        cpu_score = 0
        os.system('cls')

        hvc_validation = True
        while hvc_validation:

            print("====== Human vs CPU Mode ======\n")

            # print('='*50)
            print('\n=========================')
            print(f'{player1Name} score: {player1_score}')
            print(f'{player2Name} score: {cpu_score}')
            print('=========================\n')

            if player1_score == 10:
                os.system('cls')
                print(f'{player1Name} won! Congrats! Maybe next time {player2Name}!')
                time.sleep(4)
                quit()

            if cpu_score == 10:
                os.system('cls')
                print(f'{player2Name} won! Congrats! Maybe next time {player1Name}!')
                time.sleep(4)
                quit()

            player1Choice = input(f"{player1Name}, make a choice (R/P/S): ")


            combinations = ['R', 'P', 'S']

            cpuChoice = random.choice(combinations)


            if player1Choice == cpuChoice: # Both players chose the same option, it's a tie
                print("\n> Draw!")
                time.sleep(2)
                os.system('cls')
                player1_score += 1
                cpu_score += 1
                hvc_validation = True

            elif player1Choice in ['R','r'] and cpuChoice in ['S','s']: # Player 1 selected Rock, Player 2 selected Scissors, Player 1 wins
                print(f'\nCPU chose: {cpuChoice}')
                print(f'\n> {player1Name} wins! Congrats!')
                time.sleep(2)
                os.system('cls')
                player1_score += 1
                hvc_validation = True

            elif player1Choice in ['R','r'] and cpuChoice in ['P','p']: # Player 1 selected Rock, CPU selected Paper, CPU wins
                print(f'\nCPU chose: {cpuChoice}')
                print(f'\n> {player2Name} wins! Maybe next time!')
                time.sleep(2)
                os.system('cls')
                cpu_score += 1
                hvc_validation = True

            elif player1Choice in ['P','p'] and cpuChoice in ['R','r']: # Player 1 selected Paper, CPU selected Rock, Player 1 wins
                print(f'\nCPU chose: {cpuChoice}')
                print(f'\n> {player1Name} wins! Congrats!')
                time.sleep(2)
                os.system('cls')
                player1_score += 1
                hvc_validation = True

            elif player1Choice in ['P','p'] and cpuChoice in ['S','s']: # Player 1 selected Paper, CPU selected Scissors, CPU wins
                print(f'\nCPU chose: {cpuChoice}')
                print(f'\n> {player2Name} wins! Maybe next time!')
                time.sleep(2)
                os.system('cls')
                cpu_score += 1
                hvc_validation = True

            elif player1Choice in ['S','s'] and cpuChoice in ['P','p']: # Player 1 selected Scissors, Player 2 selected Paper, Player 1 wins
                print(f'\nCPU chose: {cpuChoice}')
                print(f'\n> {player1Name} wins! Congrats!')
                time.sleep(2)
                os.system('cls')
                player1_score += 1
                hvc_validation = True

            elif player1Choice in ['S','s'] and cpuChoice in ['R','r']: # Player 1 selected Scissors, CPU selected Rock, CPU wins
                print(f'\nCPU chose: {cpuChoice}')
                print(f'\n> {player2Name} wins! Maybe next time!')
                time.sleep(2)
                os.system('cls')
                cpu_score += 1
                hvc_validation = True

            else: # If an invalid choice is made
                print('\n> Invalid choice')
                time.sleep(2)
                os.system('cls')
                hvc_validation = True

    except KeyboardInterrupt: # KeyboardInterrupt exception gets you back to main menu
        print("\n\n--> EXITING <--")
        time.sleep(2)
        os.system('cls')
        hvc_validation = False
    
    except ValueError: # ValueError exception re-runs the function
        print("\n\n--> INVALID INPUT")
        time.sleep(2)
        os.system('cls')
        hvc_validation = True

# ===============================================================================================================================================================================

def humanVsHuman(): # Human vs Human game mode
    try:
        print("====== Human vs Human Mode ======\n")
        player1Name = input("Player 1 name: ")
        player2Name = input("Player 2 name: ")
        os.system('cls')
        player1_score = 0
        player2_score = 0

        hvh_validation = True
        while hvh_validation:
            print("====== Human vs Human Mode ======\n")


            print('\n=========================')
            print(f'{player1Name} score: {player1_score}')
            print(f'{player2Name} score: {player2_score}')
            print('=========================\n')
            # print('='*50)

            if player1_score == 10:
                os.system('cls')
                print(f'{player1Name} won! Congrats! Maybe next time {player2Name}!')
                time.sleep(4)
                quit()

            if player2_score == 10:
                os.system('cls')
                print(f'{player2Name} won! Congrats! Maybe next time {player1Name}!')
                time.sleep(4)
                quit()

            player1Choice = input(f"{player1Name}, make a choice (R/P/S): ")


            player2Choice = input(f"\n{player2Name}, make a choice (R/P/S): ")

            if player1Choice == player2Choice: # Both players chose the same option, it's a tie
                print("\n> Draw!")
                time.sleep(2)
                os.system('cls')
                player1_score += 1
                player2_score += 1
                hvh_validation = True

            elif player1Choice in ['R','r'] and player2Choice in ['S','s']: # Player 1 selected Rock, Player 2 selected Scissors, Player 1 wins
                print(f'\n> {player1Name} wins! Congrats!')
                time.sleep(2)
                os.system('cls')
                player1_score += 1
                hvh_validation = True

            elif player1Choice in ['R','r'] and player2Choice in ['P','p']: # Player 1 selected Rock, Player 2 selected Paper, Player 2 wins
                print(f'\n> {player2Name} wins! Congrats!')
                time.sleep(2)
                os.system('cls')
                player2_score += 1
                hvh_validation = True

            elif player1Choice in ['P','p'] and player2Choice in ['R','r']: # Player 1 selected Paper, Player 2 selected Rock, Player 1 wins
                print(f'\n> {player1Name} wins! Congrats!')
                time.sleep(2)
                os.system('cls')
                player1_score += 1
                hvh_validation = True

            elif player1Choice in ['P','p'] and player2Choice in ['S','s']: # Player 1 selected Paper, Player 2 selected Scissors, Player 2 wins
                print(f'\n> {player2Name} wins! Congrats!')
                time.sleep(2)
                os.system('cls')
                player2_score += 1
                hvh_validation = True

            elif player1Choice in ['S','s'] and player2Choice in ['P','p']: # Player 1 selected Scissors, Player 2 selected Paper, Player 1 wins
                print(f'\n> {player1Name} wins! Congrats!')
                time.sleep(2)
                os.system('cls')
                player1_score += 1
                hvh_validation = True

            elif player1Choice in ['S','s'] and player2Choice in ['R','r']: # Player 1 selected Scissors, Player 2 selected Rock, Player 2 wins
                print(f'\n> {player2Name} wins! Congrats!')
                time.sleep(2)
                os.system('cls')
                player2_score += 1
                hvh_validation = True

            else:
                print('\n> Invalid choice')
                time.sleep(2)
                os.system('cls')
                hvh_validation = True

    except KeyboardInterrupt:
        print("\n\n--> EXITING <--")
        time.sleep(2)
        os.system('cls')
        hvh_validation = False
    
    except ValueError:
        print("\n\n--> INVALID INPUT")
        time.sleep(2)
        os.system('cls')
        hvh_validation = True

# ===============================================================================================================================================================================


def main():
    validation = True
    while validation:
        try:
            print('''

██████╗  ██████╗  ██████╗██╗  ██╗       ██████╗  █████╗ ██████╗ ███████╗██████╗        ███████╗ ██████╗██╗███████╗███████╗ ██████╗ ██████╗ ███████╗
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝       ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗       ██╔════╝██╔════╝██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
██████╔╝██║   ██║██║     █████╔╝        ██████╔╝███████║██████╔╝█████╗  ██████╔╝       ███████╗██║     ██║███████╗███████╗██║   ██║██████╔╝███████╗
██╔══██╗██║   ██║██║     ██╔═██╗        ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗       ╚════██║██║     ██║╚════██║╚════██║██║   ██║██╔══██╗╚════██║
██║  ██║╚██████╔╝╚██████╗██║  ██╗▄█╗    ██║     ██║  ██║██║     ███████╗██║  ██║▄█╗    ███████║╚██████╗██║███████║███████║╚██████╔╝██║  ██║███████║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝    ╚══════╝ ╚═════╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
* To get out from a game mode, just press Ctrl+C combination
* To get out from the game, type 'exit' when asked for game mode
* If you get 'Draw!', a point will be added to each player
==========================================================================================================================================================''')

            print('''
    1. Human🧑 vs Human🧑
    2. Human🧑 vs CPU🤖''')

            choose_mode = input("\n> Choose a game mode: ")

            # choose_mode = int(choose_mode)
        
            if choose_mode not in ['1', '2', 'exit']:
                print("\n--> Invalid game mode specified")
                time.sleep(2)
                os.system('cls')
                validation = True

            if choose_mode == 'exit':
                print("\n--> Exiting")
                time.sleep(3)
                exit()

            if choose_mode == '1':
                os.system('cls')
                humanVsHuman()
                os.system('cls')
                validation = True
            
            elif choose_mode == '2':
                os.system('cls')
                cpuVsHuman()
                os.system('cls')
                validation = True

        except ValueError:
            print("\n\n--> Invalid Input! Try Again! <--")
            time.sleep(4)
            os.system('cls')
            validation = True
        
        except KeyboardInterrupt:
            print("\n\n> Keyboard Interrupt triggered! Aborting execution!")
            time.sleep(2)
            exit()

if __name__ == '__main__':
    main()


