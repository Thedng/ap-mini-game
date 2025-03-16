import math
import random
#creat parent class
class parentClass:
    def __init__(self,positionx,positiony,icon):
        self.positionx = positionx
        self.positiony = positiony
        self.icon = icon

    def set_position(self):
        self.positionx = round(random.randrange(50, 750), -1)
        self.positiony = round(random.randrange(50, 550), -1)

    def move(self,direction,forward):
        if direction:
            if forward:
                self.positionx += 10
            else:
                self.positionx -= 10
        else:
            if forward:
                self.positiony += 10
            else:
                self.positiony -= 10

#creat plyer class
class Player(parentClass):
    def __init__(self,name,positionx,positiony,icon):
        super().__init__(positionx,positiony,icon)
        self.name = name
        self.score = 0
        self.timer = 60
        self.shots = [[positionx,positiony]]
        self.bullets = 10
        self.lastShot = False

    def shoot(self):
        self.shots.append([self.positionx,self.positiony])
        self.bullets -= 1

    def set_score(self,p1,p2):
        score = round(math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2),-1)
        if score < 30 :
            self.score += 1
        elif score < 60 :
            self.score += 2
        elif score < 80 :
            self.score += 3
        elif score < 100 :
            self.sore += 4
        else:
            self.score += 5

    def score_prize(self):
        self.score += 10

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
