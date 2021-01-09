from random import randint

a = input('Player A, Please enter your name:')
b = 'Computer'
c = ['rock', 'paper', 'scissor']
b_input = c[randint(0, 2)]
print(f'\nHello {a} ,welcome to the Rock-Paper-Scissor game.\ninputs allowed :Rock/rock,Paper/paper,Scissor/scissor \n')
def game():
    while True:
        s1 = input(f"{a},shoot now:").lower()
        if s1 in c:
            if s1 == b_input:
                print("Ohh! Dear, its a tie,shoot again.")
                continue
            elif (s1 == 'rock' and b_input == 'paper') or (s1 == 'scissor' and b_input == 'rock') or (s1 == 'paper'and b_input == 'scissor'):
                print(f'\n ohh! you lost \n{a},better luck next time\n{b} input was {b_input}')
                break
            elif (s1 == 'paper' and b_input == 'rock') or (s1 == 'rock' and b_input == 'scissor') or (s1 == 'scissor' and b_input == 'paper'):
                print(f'\nCongratulations! {a} you won\n{b} input was {b_input}')
                break
            else:
                print('Please try to use either lower case or upper case of first letter or check your spelling.')
                break
        else:
            print('It seems you don\'t know the terms of the game,Please learn and try again')
            continue
game()
while True:
    pa = input('\nDo you want to play again?')
    response = ['yes', 'y']
    if pa.lower() in response:
        print('Great')
        game()
    else:
        print('Thanks for playing')
        break
