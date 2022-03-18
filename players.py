from turtle import Turtle



class UserShip(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.shapesize(stretch_wid=2)
        self.color("#65FFD2")
        self.penup()
        self.goto(x=0, y=-250)
        self.setheading(to_angle=90.0)
        self.laser_xcor = 0
        self.ammo = []
        self.spent_ammo = []
        for shot in range(1000):
            laser = self.simple_shooter()
            self.ammo.append(laser)

    def move_left(self):
        current_x = self.xcor()
        future_x = current_x - 15
        if future_x < -320:
            pass
        else:
            self.setx(future_x)
            for a in self.ammo:
                if a.fillcolor() != "red":
                    a.setx(future_x)

    def move_right(self):
        current_x = self.xcor()
        future_x = current_x + 15
        if future_x > 320:
            pass
        else:
            self.setx(future_x)
            for a in self.ammo:
                if a.fillcolor() != "red":
                    a.setx(future_x)

    def fire_laser(self):
        laser = self.ammo[-1]
        laser.showturtle()
        laser.color("red")

    def laser_motion(self):
        if self.ammo[-1].fillcolor() == "red":
            new_y = self.ammo[-1].ycor() + 20
            self.ammo[-1].sety(new_y)
            if self.ammo[-1].ycor() > 400:
                self.ammo[-1].hideturtle()
                self.ammo[-1].goto(0, -250)
                spent = self.ammo.pop()
                self.spent_ammo.append(spent)

    def laser_hit(self, laser):
        laser.color("black")
        laser.speed("fastest")
        laser.goto(x=1000, y=1000)
        spent = self.ammo.pop()
        self.spent_ammo.append(spent)

    def simple_shooter(self):
        ammo = Turtle()
        ammo.penup()
        ammo.shape("square")
        ammo.hideturtle()
        ammo.goto(self.position())
        ammo.setheading(90)
        return ammo

    def hit(self):
        self.hideturtle()

    def reset(self):
        self.shape("triangle")
        self.shapesize(stretch_wid=2)
        self.color("#65FFD2")
        self.penup()
        self.goto(x=0, y=-250)
        self.setheading(to_angle=90.0)
        self.laser_xcor = 0
        self.ammo = []
        self.spent_ammo = []
        for shot in range(1000):
            laser = self.simple_shooter()
            self.ammo.append(laser)




