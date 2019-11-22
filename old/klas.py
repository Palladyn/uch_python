class Unit():
    def __init__(self, name, ranc, race):
        self.name=name
        self.ranc=ranc
        self.race=race
        self.helth=100
    def show_hero(self):
        par=[]
        par.append(self.name)
        par.append(self.ranc)
        par.append(self.race)

        #param=(self.name+" "+self.ranc+" "+self.race+ " "+ str(self.helth))
        return par


class Sunit(Unit):
    def __init__(self,name,ranc,race,mlvl):
        super().__init__(name,ranc,race)
        self.mlvl=mlvl
        self.man=100

    def usemag(self,p):
        self.man=self.man-p

    def show_hero(self):
        par = []
        par.append(self.name)
        par.append(self.ranc)
        par.append(self.race)
        par.append(self.mlvl)
        par.append(self.man)

        # param=(self.name+" "+self.ranc+" "+self.race+ " "+ str(self.helth))
        return par



petro=Unit("Ivan","Hero","Varvar")
x=petro.show_hero()
print(x)

mag=Sunit("bes","vrag","nejit","15")
mag.usemag(15)
mag.usemag(30)
print(mag.show_hero())

