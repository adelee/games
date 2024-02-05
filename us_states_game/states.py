from turtle import Turtle


class States(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def publish(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.goto(self.x, self.y)
        self.write(self.state, align="center", font=("Courier", 10, "normal"))
