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
def reroll_dice(dicelist,playername):
    while (1>0):
        msg=input(playername+', do you want to reroll? Enter yes/no: ')
        if msg=='yes':
            break
        elif msg=='no':
            return dicelist
        else:
            continue
    print('Which dice do you want to reroll?')
    reroll_list=[]
    reroll_str=''
    for i in range(0,len(dicelist)):
        tmp=0
        while(1>0):
            msg=input('Enter one number of the dice you want to reroll: ')
            if int(msg) in range(1,len(dicelist)+1):
                tmp=int(msg)-1
                if (tmp in reroll_list):
                    input('You have entered this number, press enter to enter another number')
                    continue
                else:
                    reroll_list.append(tmp)
                    reroll_str=reroll_str+'number '+str(tmp+1)+': '+dicelist[tmp]+', '
                    print('You want to reroll: '+reroll_str)
                    break
            else:
                continue
        
        while(1>0):
            ind=0
            msg=input('Do you want to deselect dices?  Enter yes/no: ')
            if msg=='no':
                break
            elif msg=='yes':
                for i in range(0,len(reroll_list)):
                    while(1>0):
                        msg=input('Enter one number of the dice you want to deselect: ')
                        if (int(msg)-1 in reroll_list):
                            tmp=int(msg)-1
                            reroll_list.remove(tmp)
                            reroll_str=''
                            for x in reroll_list:
                                reroll_str=reroll_str+'number '+str(x+1)+': '+dicelist[x]+', '
                            print('You want to reroll: '+reroll_str)
                            break
                        else:
                            continue
                    while(1>0):
                        msg=input('Do you want to end dice deselection? Enter yes/no: ')
                        if msg=='yes':
                            ind=1
                            break
                        elif msg=='no':
                            break
                        else:
                            continue
                    if ind==1:
                        break
                if ind==1:
                    break
            else:
                continue
            
        while(1>0):
            msg=input('Do you want to end dice selection? Enter yes/no: ')
            if msg=='yes':
                for j in reroll_list:
                    idx=random.randint(0, 7)
                    dicelist[j]=dice_kind[idx]
                return dicelist
            elif msg=='no':
                break
            else:
                continue
        if len(reroll_list)==len(dicelist):
            dicelist=roll_dice(len(dicelist))
            return dicelist
    return
            


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
        
if __name__=='__main__':
    dicelist=['a','a','a','a','a','a','a','a']
    playername='xx'
    a=reroll_dice(dicelist,playername)