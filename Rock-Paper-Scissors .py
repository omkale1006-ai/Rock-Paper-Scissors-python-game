import random

def check_win(player,computer):
    if player==computer:
        return "Tia"
    elif(player == 'R' and computer == 'S') or \
        (player == 'P' and computer == 'R') or \
        (player == 'S' and computer == 'P'):
        return "player"
    else:
        return "computer"
    
def main():
    print("Welcome to Rock paper and sezer game:-")
    print("CHOOSE:- r for the rock,p for the paper and s for sezer:-")
    player=input("Giver your option to play game:- ").upper()

    if player not in (['R','P','S']):
        print("Plase select valid option:")
        return
        
    computer= random.choice(['R','P','S'])

    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")

    winner=check_win(player,computer)

    if winner=='Tia':
        print("Its a tai")
    elif winner=='player':
        print("you win")
    else:
        print("computer win!")

# call main
main()