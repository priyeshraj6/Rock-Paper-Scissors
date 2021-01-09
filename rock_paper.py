c = ['rock','paper','scissor']
a = input('Player A, Please enter your name:')
b = input('Player B,Please enter your name:')
print(f'\nHello {a} and {b},welcome to the Rock-Paper-Scissor game.\ninputs allowed :Rock/rock,Paper/paper,Scissor/scissor \n')
def game():
    while True:
        s1,s2 = input(f"\n{a} and {b},shoot now:").lower().split(',')
        if s1 and s2 in c:
            if s1 == s2:
                print("Ohh! Dear, its a tie,shoot again.")
                continue
            elif (s1 == 'rock' and s2 == 'paper') or (s1 == 'scissor' and s2 == 'rock') or (s1 == 'paper'and s2 == 'scissor'):
                print(f'\nCongratulations! {b} you won \n{a},better luck next time')
                break
            elif (s1 == 'paper' and s2 == 'rock') or (s1 == 'rock' and s2 == 'scissor') or (s1 == 'scissor' and s2 == 'paper'):
                print(f'\nCongratulations! {a} you won \n{b},better luck next time')
                break
            else:
                print('Please try to use either lower case or upper case of first letter or check your spelling.')
                continue
        else:
            print('It seems you don\'t know the terms of the game,Please learn and try again')
            continue
game()
while True:
    pa = input('\nDo you want to play again?')
    response = ['Yes','Y','yes','y']
    if pa.lower() in response:
        print('Great')
        game()
    else:
        print('Thanks for playing')
        break
