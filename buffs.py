class buff:
    time_remain=0
    time_max=0
    def set_time(self,time):
        if time<=self.time_max:
            self.time_remain=time
        else:
            self.time_remain=self.time_max
    def get_time(self):
        return self.time_remain
    def effect(self):
        pass
    def round_end(self):
        self.set_time(self,self.get_time()-1)

class pyro_infusion(buff):
    time_max=2
    def effect(self):
        return 0,0,'normal_attack_type','pyro'

class icicle(buff):
    time_max=3
    def effect(self):
        return 2,'cyro'
    def round_end(self):
        pass
