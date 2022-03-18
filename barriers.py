from turtle import Turtle


class Barrier(Turtle):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.destroyed_blocks = []

    def create_barriers(self):
        x_counter = -100
        y_counter = -120
        b_in_row_counter = 0
        for b in range(36):
            new_block = Turtle()
            new_block.fillcolor("#65FFD2")
            new_block.shape("square")
            new_block.penup()
            new_block.goto(x_counter, y_counter)
            new_block.setheading(90)
            x_counter += 20
            self.blocks.append(new_block)
            b_in_row_counter += 1
            if b_in_row_counter == 12:
                y_counter += 20
                x_counter = -100
            elif b_in_row_counter == 24:
                y_counter += 20
                x_counter = -100

    def destroy_barrier(self, block):
        destroyed_block = self.blocks.pop(self.blocks.index(block))
        self.destroyed_blocks.append(destroyed_block)
        block.ht()
        block.goto(x=1000, y=1000)

    def reset(self):
        if len(self.blocks) > 0:
            for block in self.blocks:
                self.destroy_barrier(block)
        self.blocks = []
        self.destroyed_blocks = []
        self.create_barriers()
