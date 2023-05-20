import character
import cards
import data
import buffs
import summons

class player:
    character_list=[]
    card_list=[]
    hold_card_list=[]
    card_pile=[]
    front=0
    dice_number=8
    dice_list=[]
    priority_element=[]
    unp_element=[]
    name=''
    def __init__(self,name):
        self.character_list=[]
        self.card_list=[]
        self.hold_card_list=[]
        self.card_pile=[]
        self.front=0
        self.dice_number=8
        self.dice_list=[]
        self.priority_element=[]
        self.unp_element=[]
        self.name=name
    def add_character(self,char):
        if len(self.character_list)>=3:
            return
        if data.check_character(char):
            eval('self.character_list.append(character.'+char+'())')
    def clear_character(self):
        self.character_list=[]
    def add_card(self,char):
        if len(self.card_list)>=30:
            return
        if data.check_card(char):
            if self.card_list.count(char)>=2:
                return
            else:
                eval('self.card_list.append(cards.'+char+'())')
    def clear_card(self):
        self.card_list=[]
    def draw_card(self,number):
        pass
    def set_priority(self):
        tmp=[]
        for a in self.character_list:
            tmp.append(a.element)
        self.priority_element=list(set(tmp))
        if len(self.priority_element)==2:
            if tmp.count(self.priority_element[0])==2:
                pass
            else:
                self.priority_element.reverse()
        for ele in data.dice_kind:
            if ele not in self.priority_element:
                self.unp_element.append(ele)
        self.unp_element.remove('omni')
    def dice_sort(self):
        tmp=['omni']
        omninum=self.dice_list.count('omni')
        pyronum=self.dice_list.count('pyro')
        cyronum=self.dice_list.count('cyro')
        anemonum=self.dice_list.count('anemo')
        hydronum=self.dice_list.count('hydro')
        dendronum=self.dice_list.count('dendro')
        electronum=self.dice_list.count('electro')
        geonum=self.dice_list.count('geo')
        tmp*=omninum
        for i in self.priority_element:
            tmp2=[i]
            exec('tmp2 *='+i+'num')
            tmp.extend(tmp2)
            tmp2=[]
        for i in self.unp_element:
            tmp2=[i]
            exec('tmp2 *='+i+'num')
            tmp.extend(tmp2)
            tmp2=[]
        self.dice_list=tmp
        del tmp

def default_character(playerx):
    if isinstance(playerx,player):
        playerx.add_character('diluc')
        playerx.add_character('sucrose')
        playerx.add_character('kaeya')

def get_damage():
    pass

def apply_damage():
    pass

def check_game_end(player1,player2):
    if player1.character_list[0].hp+player1.character_list[1].hp+player1.character_list[2].hp==0:
        return True,'player2'
    if player2.character_list[0].hp+player2.character_list[1].hp+player2.character_list[2].hp==0:
        return True,'player1'
    return False,''

def gameloop(a,player1,player2):
    game_begin(player1,player2)
    begin_phase(player1,player2)
    pass
def game_begin(player1,player2):
    player1.set_priority()
    player2.set_priority()
    #draw 5 cards(after)
    pass
def begin_phase(player1,player2):
    player1.dice_list=data.roll_dice(8)
    player2.dice_list=data.roll_dice(8)
    player1.dice_sort()
    player2.dice_sort()
    print(player1.name+'\'s dice: ',end='')
    for i in player1.dice_list:
        print(i+', ',end='')
    print('')
    print(player2.name+'\'s dice: ',end='')
    for i in player2.dice_list:
        print(i+', ',end='')
    print('')
    player1.dice_list=data.reroll_dice(player1.dice_list, player1.name)
    player1.dice_sort()
    print(player1.name+'\'s dice: ',end='')
    for i in player1.dice_list:
        print(i+', ',end='')
    print('')
    player2.dice_list=data.reroll_dice(player2.dice_list, player2.name)
    player2.dice_sort()
    print(player2.name+'\'s dice: ',end='')
    for i in player2.dice_list:
        print(i+', ',end='')
    print('')
    print_scene(player1,player2)
    print_scene(player2,player1)

def action_phase_begin():
    pass
def action_phase():
    while(1>0):
        
        pass
    pass
def end_phase():
    pass

def print_scene(playerx,playery):
    if isinstance(playerx,player)&isinstance(playery,player):
        print('Your opponent: '+playery.name)
        print('Dice remaining: '+str(len(playery.dice_list)))
        print('Card remaining: '+str(len(playery.card_list)))
        for i in playery.character_list:
            print(i.name+': hp:'+str(i.hp)+', energy:'+str(i.energy),end='')
            if i.weapon!='':
                print(', weapon:'+i.weapon,end='')
            if i.talent!='':
                print(', talent:'+i.weapon,end='')
            if i.artifact!='':
                print(', artifact:'+i.weapon,end='')
            print('')
        print('')
        print('Your name: '+playerx.name)
        print('Your dice: ',end='')
        for i in playerx.dice_list:
            print(i+', ',end='')
        print('('+str(len(playerx.dice_list))+')')
        print('Your card: ',end='')
        for i in playerx.card_list:
            print(i+', ',end='')
        print('')
        for i in playerx.character_list:
            print(i.name+': hp:'+str(i.hp)+', energy:'+str(i.energy),end='')
            if i.weapon!='':
                print(', weapon:'+i.weapon,end='')
            if i.talent!='':
                print(', talent:'+i.weapon,end='')
            if i.artifact!='':
                print(', artifact:'+i.weapon,end='')
            print('')
        print('')
        
if __name__=='__main__':
    player1=player('xx')
    default_character(player1)
    player2=player('yy')
    default_character(player2)
    gameloop(0,player1,player2)