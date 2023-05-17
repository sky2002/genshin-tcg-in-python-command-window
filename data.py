import random
all_character_list=['diluc','sucrose','kaeya']
all_card_list=[]
dice_kind=['omni','pyro','cyro','anemo','hydro','dendro','electro','geo']
def roll_dice(number):
    if number>0:
        dices=[]
        for i in range(0,number):
            idx=random.randint(0, 7)
            dices.append(dice_kind[idx])
        return dices
def check_character(char):
    if char in all_character_list:
        return char in all_character_list
    else:
        return char in all_character_list
        print('Error')
def check_card(char):
    if char in all_card_list:
        return char in all_card_list
    else:
        return char in all_card_list
        print('Error')