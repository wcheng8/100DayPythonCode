class Collision():
    def __init__(self):
        self.width = 600 / 2
        self.height = 600 / 2

    def check_boundary(self, player):
        if player.xcor() > self.width - 10:
            player.goto(self.width - 10, player.ycor())
        if player.xcor() < -self.width + 10:
            player.goto(-self.width + 10, player.ycor())
        if player.ycor() < -self.height + 20:
            player.goto(player.xcor(), -self.height + 20)

    def win_condition(self, player):
        if player.ycor() > self.height:
            player.goto(player.xcor(), -self.height + 20)
            # score.level_up()

    def win_condition1(self,player):
        if player.ycor() > self.height:
            player.goto(player.xcor(),-self.height+20)
            return True