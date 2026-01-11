import random

while True:
    ask = input('Do you want to Roll the rice? (y/n) ').lower()
    if ask == 'y':
        rand1 = random.randint(1,6)
        rand2 = random.randint(1,6)
        print(f'({rand1}, {rand2})')
    elif ask == 'n':
        print('Thanks for playing')
        break
    else:
        print('Invalid! ')
