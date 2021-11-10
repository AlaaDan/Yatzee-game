import random
game_is_on = True
total_score = 0
bonus = 50
#  I thought it would take up to 8-10 hours.
#  I have spent around 15 hours.
#  The hardiest part was the round irritation, it's not hard but i totally forgot to use the argument to solve
#  my problem.

def welcome():
    print('''Welcome to Yatzy Light! 
------------------------------------- \n''')
    choice = True
    while choice:
        print('''Press "1" to play the game 
Press "2" to exit the program ''')
        user_input = input('Your choice: ')
        if user_input == "1":
            game_play(1)
            game_play(2)
            game_play(3)
            game_play(4)
            game_play(5)
            game_play(6)
            score_function()
        elif user_input == "2":
            print('''Exiting the game
            See ya later! ''')
            choice = False
        else:
            print('\nInvalid input, in order to proceed you need to, ')


def score_function():
    global total_score
    if total_score == 63 or total_score > 63:
        print(f'''Lucky you! You scored {total_score} and you got a bonus {bonus} 
    Your grand total score is [ {total_score + bonus} ]\n''')
        total_score = 0
    elif total_score < 63:
        print(f'Nice! You scored [ {total_score} ]\n')
        total_score = 0


def game_play(round):
    score = 0
    roll = 4
    die = 5
    global bonus
    global total_score
    print(f'''        ROUND {round} STARTED \n''')
    for x in range(1, roll):
        input("Push ENTER to roll the dice")
        print(f'Roll number {x} of ROUND {round}')
        dice = []
        for number in range(die):
            number = (random.randint(1, 6))
            if number == round:
                die -=1
                score += number
                total_score += number
            dice.append(number)
        dice_str = str(dice).replace("[", "").replace("]", "").replace(",", "")
        #strip_dice = dice_str.strip("[").strip("]").strip(",")
        print(f'        {dice_str}')

    print(f'Total score for round {round} is {score}')


welcome()