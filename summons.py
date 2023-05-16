class summon:
    max_usage=0
    usage=0
    element='physical'
    damage=0
    def effect(self):
        pass
    def get_usage(self):
        return self.usage
    def set_usage(self,usage):
        if usage<=self.max_usage:
            self.usage=usage
        else:
            self.usage=self.max_usage
    
class large_wind_spirit(summon):
    max_usage=3
    usage=3
    element='anemo'
    damage=2
    def when_swirl(self,s_element):
        self.element=s_element
    def effect(self):
        self.set_usage(self.get_usage()-1)
        return self.damage,self.element
    