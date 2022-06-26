import random
from secrets import choice

def paint(choice):
    if choice =='rock':
        print("""
            _______
        ---'   ____)
             (_____)
             (_____)
              (____)
        ---.__(___)
        """)

    if choice== 'paper':
        print("""
            _______
        ---'   ____)____
                  ______)
                  _______)
                _______)
        ---.__________)
        """)

    if choice=='scissors':
        print("""
            _______
        ---'   ____)____
                  ______)
             __________)
              (____)
        ---.__(___)
        """)

def game_rule(me,cpu):
    if me==cpu:
        print('draw')
    elif (   me == 'scissors' and cpu == 'rock'
        or   me == 'paper'    and cpu == 'scissors' 
        or   me == 'rock'     and cpu == 'paper'):
        print('you lose')
    else:
        print('you win')

#################  main code  #########################################
list=['rock', 'paper', 'scissors']

my_choice=int(input('choose rock[1] paper[2] scissors[3]:'))
if my_choice>3 or my_choice<1:
    print('wrong input... you lose')
else:
    computer_choice=random.randint(0,2)
    print(f'you choose {list[my_choice-1]}')
    paint(list[my_choice-1])
    print(f'computer choose {list[computer_choice]}')
    paint(list[computer_choice])
    game_rule(list[my_choice-1],list[computer_choice])
