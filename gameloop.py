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
    def dice_sort(self):
        tmp=self.dice_list
        
        self.dice_list=tmp
        del tmp
        pass

def default_character(player1):
    if isinstance(player1,player):
        player1.add_character('diluc')
        player1.add_character('sucrose')
        player1.add_character('kaeya')

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
    players=[player1,player2]
    game_begin(players)
    begin_phase(players)
    pass
def game_begin(players):
    players[0].set_priority()
    players[1].set_priority()
    #draw 5 cards(after)
    pass
def begin_phase(players):
    players[0].dice_list=data.roll_dice(8)
    players[1].dice_list=data.roll_dice(8)
    players[0].dice_sort()
    players[1].dice_sort()
    print('dice of player1: ',end='')
    print(players[0].dice_list)
    print('dice of player2: ',end='')
    print(players[1].dice_list)
    pass
def action_phase_begin():
    pass
def action_phase():
    pass
def end_phase():
    pass


player1=player()
default_character(player1)
player2=player()
default_character(player2)
gameloop(0,player1,player2)
print(data.dice_kind)