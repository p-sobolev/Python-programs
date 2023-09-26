import random

s = """balance - to check the remaining balance
payout - to see the payout table
rewards - to see the list of rewards
deposit - to deposit money
q - to start the slot machine
quit - to exit
"""

# RTP (Return-to-player) = 95%


p = """0 - 75: no win
76-90: bet x 2
91-95: bet x 3
96 - 99: bet x 5
100: bet x 25
"""

r = """deposit x 5: reward 1
deposit x 10: reward 2
deposit x 20: reward 3
"""


def multiplicator(n):
    return lambda x: x*n


win = int(0)
balance = int(0)

double = multiplicator(2)
triple = multiplicator(3)
quintuple = multiplicator(5)
jackpot = multiplicator(50)

deposit_made = False

print("Type 'help' to see the list of commands")
while True:
    player_says = input(">").lower()
    if player_says == "balance":
        print(f"{balance}$")
    elif player_says == "deposit" and deposit_made is False:
        try:
            deposit = int(input("""How much would you like to deposit? 
>"""))
            balance = balance + deposit
            print(f"your current balance is {balance}$")
            deposit_made = True
            if deposit_made is True:
                print("Deposits are no longer possible")
        except:
            print("invalid input; switching to main menu.")
    elif player_says == "q":
        while balance == 0:
            print("Your balance is zero")
            break
        else:
            bet = int(input("""How much do you wish to bet?
"""))
            if bet > balance:
                print("Insufficient funds. Lower your bet")
            else:
                balance = balance - bet
                pip = random.randint(0, 100)
                print(pip)
                if pip in range(76, 91):
                    print(f"you win: {double(bet)}!")
                    balance = balance + double(bet)
                elif pip in range(91, 96):
                    print(f"you win: {triple(bet)}!")
                    balance = balance + triple(bet)
                elif pip in range(96, 100):
                    print(f"you win: {quintuple(bet)}!")
                    balance = balance + quintuple(bet)
                elif pip == 100:
                    print("JACKPOT!!!")
                    print(f"you win: {jackpot(bet)}!!!")
                    balance = balance + jackpot(bet)
                else:
                    print("No win")
            print(f"your current balance is {balance}$")
    elif player_says == "help":
        print(s)
    elif player_says == "payout":
        print(p)
    elif player_says == "rewards":
        print(r)
    elif player_says == "quit":
        print(f"Your balance is {balance}$")
        break
    else:
        print("invalid command")