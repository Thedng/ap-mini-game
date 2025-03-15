#creat parent class
class parentClass:
    def init(self,positionx,positiony,icon):
        # self.position = (round(random.randrange(0, 800),-1), round(random.randrange(0, 600),-1))
        self.positionx = positionx
        self.positiony = positiony
        self.icon = icon

#creat plyer class
class Player(parentClass):
    def init(self,positionx,positiony,icon):
        super().init(positionx,positiony,icon)
        self.score = 0
        self.timer = 60
        self.shots = [[positionx,positiony]]
        self.bullets = 10

    def shoot(self):
        self.shots.append([self.positionx,self.positiony])
        self.bullets -= 1

    def set_score(self):
        pass

    def set_timer(self):
        pass

#creat target class
class target(parentClass):
    def init(self,positionx,positiony,icon):
        super().init(positionx,positiony,icon)

#creat bullet prize class
class bulletPrize(parentClass):
    def init(self,positionx,positiony,icon):
        super().init(positionx,positiony,icon)

#creat time prize class
class timePrize(parentClass):
    def init(self,positionx,positiony,icon):
        super().init(positionx,positiony,icon)
