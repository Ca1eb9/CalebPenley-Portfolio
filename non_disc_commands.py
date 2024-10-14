
def roll_dice(entities):
    if entities[0]['type'] == 'num':
        roll_results = []
        dice_num = 1
        if entities[0]['entity'] == 'one':
            dice_num = 1
        elif entities[0]['entity'] == 'two':
            dice_num = 2
        elif entities[0]['entity'] == 'three':
            dice_num = 3
        elif entities[0]['entity'] == 'four':
            dice_num = 4
        elif entities[0]['entity'] == 'five':
            dice_num = 5
        elif entities[0]['entity'] == 'six':
            dice_num = 6
        else:
            dice_num = int(entities[0]['entity'])
        import random
        res=''
        for _ in range(dice_num):
            roll = random.randint(1, 6)
            roll_results.append(roll)
        for i in range(len(roll_results)):
            i+=1
            if i >= 2:
                res += ', dice {i} rolled a {roll}'.format(i=i, roll=roll_results[i-1])
            else:
                res += 'Dice {i} rolled a {roll}'.format(i=i, roll=roll_results[i-1])
        return res
def pick_number(entities):
    print('hi')