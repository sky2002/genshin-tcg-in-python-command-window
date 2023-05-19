class character:
    max_hp=0
    max_energy=0
    hp=0
    energy=0
    normal_attack_damage=0
    normal_attack_type=''
    element=''
    weapon_type=''
    origin=''
    elemental_skill_damage=0
    elemental_skill_type=''
    elemental_burst_damage=0
    elemental_burst_type=''
    
    def __init__(self):
        self.max_hp=0
        self.max_energy=0
        self.hp=0
        self.energy=0
        self.normal_attack_damage=0
        self.normal_attack_type=''
        self.element=''
        self.weapon_type=''
        self.origin=''
        self.elemental_skill_damage=0
        self.elemental_skill_type=''
        self.elemental_burst_damage=0
        self.elemental_burst_type=''
    
    def set_hp(self,hp):
        self.hp=hp
        
    def get_hp(self):
        return self.hp
    
    def set_energy(self,energy):
        if energy<=self.max_energy:
            self.energy=energy
        else:
            self.energy=self.max_energy
        
    def get_energy(self):
        return self.energy
    
    def elemental_burst_available(self):
        if self.energy<self.max_energy:
            return False
        return True
        
    def normal_attack(self):
        self.set_energy(self.get_energy()+1)
        return self.normal_attack_damage,self.normal_attack_type
    
    def elemental_skill(self):
        self.set_energy(self.get_energy()+1)
        return self.elemental_skill_damage,self.elemental_skill_type
            
    def elemental_burst(self):
        if self.elemental_burst_available():
            self.set_energy(0)
            return self.elemental_burst_damage,self.elemental_burst_type
        
    def round_end(self):
        pass

class diluc(character):
    elemental_skill_times=0
    
    def __init__(self):
        self.max_hp=10
        self.max_energy=3
        self.hp=10
        self.energy=0
        self.element='pyro'
        self.weapon_type='claymore'
        self.origin='mondstadt'
        self.normal_attack_damage=2
        self.normal_attack_type='physical'
        self.elemental_skill_damage=3
        self.elemental_skill_type='pyro'
        self.elemental_skill_times=0
        self.elemental_burst_damage=8
        self.elemental_burst_type='pyro'

    def elemental_skill(self):
        self.set_energy(self.get_energy()+1)
        self.elemental_skill_times=self.elemental_skill_times+1
        if self.elemental_skill_times==3:
            return self.elemental_skill_damage+2,self.elemental_skill_type
        return self.elemental_skill_damage,self.elemental_skill_type
        
    def elemental_burst(self):
        if self.elemental_burst_available():
            self.set_energy(0)
            return self.elemental_burst_damage,self.elemental_burst_type,'buff','pyro_infusion'

    def round_end(self):
        self.elemental_skill_times=0
        
class sucrose(character):
    
    def __init__(self):
        self.max_hp=10
        self.max_energy=2
        self.hp=10
        self.energy=0
        self.element='anemo'
        self.weapon_type='catalyst'
        self.origin='mondstadt'
        self.normal_attack_damage=1
        self.normal_attack_type='anemo'
        self.elemental_skill_damage=3
        self.elemental_skill_type='anemo'
        self.elemental_burst_damage=1
        self.elemental_burst_type='anemo'
    
    def elemental_skill(self):
        self.set_energy(self.get_energy()+1)
        return self.elemental_skill_damage,self.elemental_skill_type,'move','-1'
        
    def elemental_burst(self):
        if self.elemental_burst_available():
            self.set_energy(0)
            return self.elemental_burst_damage,self.elemental_burst_type,'summon','large_wind_spirit'
    
class kaeya(character):
    
    def __init__(self):
        self.max_hp=10
        self.max_energy=2
        self.hp=10
        self.energy=0
        self.element='cyro'
        self.weapon_type='sword'
        self.origin='mondstadt'
        self.normal_attack_damage=2
        self.normal_attack_type='physical'
        self.elemental_skill_damage=3
        self.elemental_skill_type='cyro'
        self.elemental_burst_damage=1
        self.elemental_burst_type='cyro'
            
    def elemental_burst(self):
        if self.elemental_burst_available():
            self.set_energy(0)
            return self.elemental_burst_damage,self.elemental_burst_type,'buff','icicle'



