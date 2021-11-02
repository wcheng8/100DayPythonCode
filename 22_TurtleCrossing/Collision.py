class collision():
    def __init__(self):
        self.width = 600/2
        self.height = 600/2

    def check_boundary(self,player,score):
        if player.xcor() > self.width-10:
            player.goto(self.width-10, player.ycor())
        if player.xcor() < -self.width+10:
            player.goto(-self.width+10, player.ycor())
        if player.ycor() > self.height:
            player.goto(player.xcor(), -self.height+20)
            score.level_up()
        if player.ycor() < -self.height+20:
            player.goto(player.xcor(), -self.height+20)

