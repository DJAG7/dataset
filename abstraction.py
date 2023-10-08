class car:
    def __init__(self,colour,maker,topspeed):
        self.colour=colour
        self.maker=maker
        self.topspeed=topspeed

    def quality(self):
        if (self.maker == "BMW"):
            print("bad")
        else:
            if (self.topspeed>100):
                print ("good")

pCar= car("black","thar",105)
pCar.quality()

#abstraction