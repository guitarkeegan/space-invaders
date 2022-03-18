from turtle import Turtle

FONT = ("Ariel", 46, "normal")
PLAY_AGAIN = "Would you like to play again?"

class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.pencolor("white")

    def level_completed(self):
        message = "You have completed the level!"

        self.write(message + "\n" + "   (dance break!)" + "\n" + PLAY_AGAIN, align="center", font=FONT)

    def game_over(self):
        message = "Your ship has been destroyed!" + "\n" "Would you like to play again? y or n: "
        self.write(message, align="center", font=FONT)

    def reset(self):
        self.clear()
