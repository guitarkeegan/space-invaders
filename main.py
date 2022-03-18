import turtle
import playsound
from turtle import Screen
from players import UserShip
from aliens import Aliens
from time import time
from messages import Message
from barriers import Barrier

screen = Screen()
screen.bgcolor("black")
screen.colormode(255)

screen.tracer(0)
messenger = Message()
barrier = Barrier()
barrier.create_barriers()
aliens = Aliens(5)
ship = UserShip()
screen.onkeypress(ship.move_left, ",")
screen.onkeypress(ship.move_right, ".")
screen.onkeypress(ship.fire_laser, "f")
screen.listen()
playsound.playsound("Nague.mp3", False)


# tempo 135 ish

def game_reset():
    aliens.reset()
    messenger.reset()
    ship.reset()
    ship.showturtle()
    barrier.reset()


on = True
start = time()
alien_shift = []
# about 2 hours of time. 60sec * 120min, 7200sec / 1.2sec approx. tempo 6000 in list
for _ in range(6000):
    shift = start + 1.2
    alien_shift.append(shift)
    start += 1.2
print(alien_shift[:3])
index = 0
while on:
    screen.update()
    ship.laser_motion()
    aliens.laser_motion()

    for alien in aliens.living_aliens:
        if alien.distance(ship.ammo[-1]) < 20:
            ship.laser_hit(ship.ammo[-1])
            aliens.destroy_alien(alien)

    if round(time(), 1) == round(alien_shift[index], 1):
        index += 1
        if aliens.alien_progress_counter % 2 == 0:
            aliens.alien_shuffle_left()
        else:
            aliens.alien_shuffle_right()

    # beat level
    if len(aliens.living_aliens) == 0:
        messenger.level_completed()

    # destroy barrier blocks
    for block in barrier.blocks:
        if block.distance(ship.ammo[-1]) < 20:
            ship.laser_hit(ship.ammo[-1])
            barrier.destroy_barrier(block)
        if block.distance(aliens.lasers[-1]) < 20 and aliens.lasers[-1].isvisible():
            aliens.laser_hit()
            barrier.destroy_barrier(block)

    # game over
    if ship.distance(aliens.lasers[-1]) < 40:
        ship.hit()
        messenger.game_over()

    # make keys available
    if not ship.isvisible():
        screen.onkeypress(turtle.bye, "n")
        screen.onkeypress(game_reset, "y")

screen.exitonclick()
