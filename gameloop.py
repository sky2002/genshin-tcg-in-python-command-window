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
    def __init__(self):
        self.character_list=[]
        self.card_list=[]
        self.hold_card_list=[]
        self.card_pile=[]
        self.front=0
        self.dice_number=8
        self.dice_list=[]
        self.priority_element=[]
        self.unp_element=[]
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
    def set_unp(self):
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
    player1.set_unp()
    player2.set_unp()
    #draw 5 cards(after)
    pass
def begin_phase(player1,player2):
    player1.dice_list=data.roll_dice(8)
    player2.dice_list=data.roll_dice(8)
    player1.dice_sort()
    player2.dice_sort()
    print('dice of player1: ',end='')
    print(player1.dice_list)
    print('dice of player2: ',end='')
    print(player2.dice_list)
    player1.dice_list=data.reroll_dice(player1.dice_list, 'player1')
    player1.dice_sort()
    print('dice of player1: ',end='')
    print(player1.dice_list)
    player2.dice_list=data.reroll_dice(player2.dice_list, 'player2')
    player2.dice_sort()
    print('dice of player2: ',end='')
    print(player2.dice_list)
    

def action_phase_begin():
    pass
def action_phase():
    pass
def end_phase():
    pass

if __name__=='__main__':
    player1=player()
    default_character(player1)
    player2=player()
    default_character(player2)
    gameloop(0,player1,player2)