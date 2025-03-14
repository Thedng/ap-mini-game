#creat parent class
class parentClass:
    def __init__(self,positionx,positiony,icon):
        # self.position = (round(random.randrange(0, 800),-1), round(random.randrange(0, 600),-1))
        self.positionx = positionx
        self.positiony = positiony
        self.icon = icon

#creat plyer class
class Player(parentClass):
    def __init__(self,positionx,positiony,icon):
        super().__init__(positionx,positiony,icon)
        self.score = 0
        self.timer = 60
        self.shots = []
        self.bullets = 10
    def move(self):
        pass

    def shoot(self):
        self.shots.append(self.position)
        self.bullets -= 1
        return self.position

    def set_score(self):
        pass

    def set_timer(self):
        pass

#creat target class
class target(parentClass):
    def __init__(self,positionx,positiony,icon):
        super().__init__(positionx,positiony,icon)

#creat bullet prize class
class bulletPrize(parentClass):
    def __init__(self,positionx,positiony,icon):
        super().__init__(positionx,positiony,icon)

#creat time prize class
class timePrize(parentClass):
    def __init__(self,positionx,positiony,icon):
        super().__init__(positionx,positiony,icon)
