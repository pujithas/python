class person:
    def set(self,first,last):
        self.first=first
        self.last=last
    def get(self):
        print(self.first,"firstname")
        print(self.last,"lastname")
        
personname=person()
personname.set("pujitha","galla")
personname.get()
