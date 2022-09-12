import os
import time


def humanVsHuman():
    try:
        print("====== Human vs Human Mode ======\n")
        player1Name = input("Player 1 name: ")
        player2Name = input("Player 2 name: ")
        os.system('cls')

        hvh_validation = True
        while hvh_validation:
            print("====== Human vs Human Mode ======\n")

            # print('='*50)

            player1Choice = input(f"{player1Name}, make a choice (R/P/S): ")


            player2Choice = input(f"\n{player2Name}, make a choice (R/P/S): ")


            if player1Choice == player2Choice: # Both players chose the same option, it's a tie
                print("\n> Draw!")
                time.sleep(4)
                os.system('cls')
                hvh_validation = True

            elif player1Choice in ['R','r'] and player2Choice in ['S','s']: # Player 1 selected Rock, Player 2 selected Scissors, Player 1 wins
                print(f'\n> {player1Name} wins! Congrats!')
                time.sleep(4)
                os.system('cls')
                hvh_validation = True

            elif player1Choice in ['R','r'] and player2Choice in ['P','p']: # Player 1 selected Rock, Player 2 selected Paper, Player 2 wins
                print(f'\n> {player2Name} wins! Congrats!')
                time.sleep(4)
                os.system('cls')
                hvh_validation = True

            elif player1Choice in ['P','p'] and player2Choice in ['R','r']: # Player 1 selected Paper, Player 2 selected Rock, Player 1 wins
                print(f'\n> {player1Name} wins! Congrats!')
                time.sleep(4)
                os.system('cls')
                hvh_validation = True

            elif player1Choice in ['P','p'] and player2Choice in ['S','s']: # Player 1 selected Paper, Player 2 selected Scissors, Player 2 wins
                print(f'\n> {player2Name} wins! Congrats!')
                time.sleep(4)
                os.system('cls')
                hvh_validation = True

            elif player1Choice in ['S','s'] and player2Choice in ['P','p']: # Player 1 selected Scissors, Player 2 selected Paper, Player 1 wins
                print(f'\n> {player1Name} wins! Congrats!')
                time.sleep(4)
                os.system('cls')
                hvh_validation = True

            elif player1Choice in ['S','s'] and player2Choice in ['R','r']: # Player 1 selected Scissors, Player 2 selected Rock, Player 2 wins
                print(f'\n> {player2Name} wins! Congrats!')
                time.sleep(4)
                os.system('cls')
                hvh_validation = True

            else:
                print('\n> Invalid choice')
                time.sleep(4)
                os.system('cls')
                hvh_validation = True

    except KeyboardInterrupt:
        print("\n\n--> EXITING <--")
        time.sleep(2)
        os.system('cls')
        quit()
    
    except ValueError:
        print("\n\n--> INVALID INPUT")
        time.sleep(2)
        os.system('cls')
        hvh_validation = True

