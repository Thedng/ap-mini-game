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
        self._score = 0
        self._timer = 120
        self.shots = [[positionx,positiony]]
        self._bullets = 25
        self.lastShot = False

    def shoot(self):
        self.shots.append([self.positionx,self.positiony])
        self._bullets -= 1

    def set_score(self,p1,p2):
        score = round(math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2),-1)
        if score < 30 :
            self._score += 1
        elif score < 60 :
            self._score += 2
        elif score < 80 :
            self._score += 3
        elif score < 100 :
            self._score += 4
        else:
            self._score += 5

    def score_prize(self):
        self._score += 10

    def set_bonus(self):
        rand_num = random.randrange(1,5)
        if rand_num == 1 :
            self._bullets += 3
        elif rand_num == 2 :
            self._bullets += 5
        elif rand_num == 3 :
            self._timer += 10
        else :
            self._timer += 20

    def dec_timer(self):
        self._timer -= 1

    def have_bullets(self):
        return self._bullets > 0

    def have_timer(self):
        return self._timer > 0

    def get_score(self):
        return self._score

    def get_timer(self):
        return self._timer

    def get_bullets(self):
        return self._bullets

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
