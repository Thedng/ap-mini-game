#creat parent class
class parentClass:
    def __init__(self,positionx,positiony):
        # self.position = (round(random.randrange(0, 800),-1), round(random.randrange(0, 600),-1))
        self.position = (positionx,positiony)

#creat plyer class
class Player(parentClass):
    def __init__(self,positionx,positiony):
        super().__init__(positionx,positiony)
        self.score = 0
        self.timer = 0
    def move(self):
        pass

    def shoot(self):
        pass

    def set_score(self):
        pass

    def set_timer(self):
        pass

#creat target class
class target(parentClass):
    def __init__(self,positionx,positiony):
        super().__init__(positionx,positiony)
        self.icon = 'icon/target.png'

#creat bullet prize class
class bulletPrize(parentClass):
    def __init__(self,positionx,positiony):
        super().__init__(positionx,positiony)

#creat time prize class
class timePrize(parentClass):
    def __init__(self,positionx,positiony):
        super().__init__(positionx,positiony)
