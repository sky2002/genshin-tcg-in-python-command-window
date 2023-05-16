class character:
    max_hp=0
    max_energy=0
    hp=0
    energy=0
    normal_attack_damage=0
    normal_attack_type=''
    elemental_skill_damage=0
    elemental_skill_type=''
    elemental_burst_damage=0
    elemental_burst_type=''
    def _init_ (self,hp,energy):
        self.hp=0
        self.energy=0
    
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
    max_hp=10
    max_energy=3
    hp=10
    energy=0
    normal_attack_damage=2
    normal_attack_type='physical'
    elemental_skill_damage=3
    elemental_skill_type='pyro'
    elemental_skill_times=0
    elemental_burst_damage=8
    elemental_burst_type='pyro'

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
    max_hp=10
    max_energy=2
    hp=10
    energy=0
    normal_attack_damage=1
    normal_attack_type='anemo'
    elemental_skill_damage=3
    elemental_skill_type='anemo'
    elemental_burst_damage=1
    elemental_burst_type='anemo'
    
    def elemental_skill(self):
        self.set_energy(self.get_energy()+1)
        return self.elemental_skill_damage,self.elemental_skill_type,'move','-1'
        
    def elemental_burst(self):
        if self.elemental_burst_available():
            self.set_energy(0)
            return self.elemental_burst_damage,self.elemental_burst_type,'summon','large_wind_spirit'
    
class kaeya(character):
    max_hp=10
    max_energy=2
    hp=10
    energy=0
    normal_attack_damage=2
    normal_attack_type='physical'
    elemental_skill_damage=3
    elemental_skill_type='cyro'
    elemental_burst_damage=1
    elemental_burst_type='cyro'
            
    def elemental_burst(self):
        if self.elemental_burst_available():
            self.set_energy(0)
            return self.elemental_burst_damage,self.elemental_burst_type,'buff','icicle'



