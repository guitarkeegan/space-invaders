from turtle import Turtle
import random


class Aliens(Turtle):
    def __init__(self, top_row_num):
        super().__init__()
        self.living_aliens = []
        self.dead_aliens = []
        self.px_height_width = 20
        self.row_ycor = [320, 290, 260, 230, 200, 170]
        self.even_xcor = [-20, 20, 60, -60, 100, -100]
        self.odd_xcor = [0, 40, -40, 80, -80]
        self.alien_positions = [(0, 170),
                                (-20, 200), (20, 200),
                                (0, 230), (40, 230), (-40, 230),
                                (-20, 260), (20, 260), (60, 260), (-60, 260),
                                (0, 290), (40, 290), (-40, 290), (80, 290), (-80, 290),
                                (-20, 320), (20, 320), (60, 320), (-60, 320), (100, 320), (-100, 320)]
        # self.create_wedge(top_row_num)
        self.make_v(top_row_num)
        self.alien_progress_counter = 2
        self.lasers = []
        self.make_lasers()
        self.spent_lasers = []

    def alien_shuffle_left(self):
        for alien in self.living_aliens:
            old_x = alien.xcor()
            new_x = old_x - 30
            alien.setx(new_x)
            if new_x < -320:
                self.alien_progress_counter += 1
        chance_to_fire = random.randint(0, 10)
        if chance_to_fire < 5:
            self.shoot_laser()

    def alien_shuffle_right(self):
        for alien in self.living_aliens:
            old_x = alien.xcor()
            new_x = old_x + 30
            alien.setx(new_x)
            if new_x > 320:
                self.alien_progress_counter += 1
        chance_to_fire = random.randint(0, 10)
        if chance_to_fire < 5:
            self.shoot_laser()

    def destroy_alien(self, alien):
        da = self.living_aliens.pop(self.living_aliens.index(alien))
        self.dead_aliens.append(da)
        alien.color("black")
        alien.speed("fastest")
        alien.goto(x=1000, y=1000)

    def make_v(self, odd_num):
        if odd_num % 2 == 0:
            pass
        else:
            places = []
            counter = 0
            for n in range(odd_num):
                places.append(0 + counter)
                places.append(0 - counter)
                counter += 30
            places.pop(0)
            ycor = 170
            v_counter = 0
            for xcor in places:
                alien = self.make_aliens()
                alien.goto(x=xcor, y=ycor)
                v_counter += 1
                if v_counter % 2 != 0:
                    ycor += 30

    def make_aliens(self):
        alien = Turtle()
        alien.hideturtle()
        alien.penup()
        alien.shape("square")
        alien.setheading(270)
        alien.color("purple")
        alien.showturtle()
        self.living_aliens.append(alien)
        return alien

    def make_lasers(self):
        for lasers in range(10):
            laser = Turtle()
            laser.shape("circle")
            laser.hideturtle()
            laser.speed("fastest")
            laser.goto(0, 300)
            laser.setheading(270)
            self.lasers.append(laser)

    def shoot_laser(self):
        alien_to_fire = random.choice(self.living_aliens)
        laser_to_fire = self.lasers[-1]
        laser_to_fire.goto(alien_to_fire.xcor(), alien_to_fire.ycor())
        laser_to_fire.showturtle()
        laser_to_fire.fillcolor("red")

    def laser_motion(self):
        if self.lasers[-1].isvisible():
            new_y = self.lasers[-1].ycor() - 15
            self.lasers[-1].sety(new_y)
            if self.lasers[-1].ycor() < -400:
                spent = self.lasers.pop(-1)
                spent.fillcolor("black")
                spent.hideturtle()
                spent.goto(0, 300)
                self.lasers.append(spent)

    def laser_hit(self):
        self.lasers[-1].hideturtle()
        self.lasers[-1].fillcolor("black")
        self.lasers[-1].speed("fastest")
        self.lasers[-1].goto(x=0, y=300)
        spent = self.lasers.pop()
        self.lasers.append(spent)

    def reset(self):
        if len(self.living_aliens) > 0:
            for alien in self.living_aliens:
                alien.hideturtle()
                alien.goto(1000, 1000)
            for laser in self.lasers:
                laser.hideturtle()
                laser.goto(1000, 1000)
        self.dead_aliens = []
        self.living_aliens = []
        self.make_v(5)
        self.alien_progress_counter = 2
        self.lasers = []
        self.make_lasers()
        self.spent_lasers = []
