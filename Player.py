from GameObject import GameObject

class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'images/Player.png')
    self.dx = 0
    self.dy = 0
    self.reset()

  def left(self):
    if 25 <= self.x <= 65:
        self.dx -= 25
    elif self.x < 25:
        self.right()
        self.dx -= 100
    else:
        self.dx -= 100

  def right(self):
    if 335 >= self.x >= 290:
        self.dx += 25
    elif self.x > 335:
        self.left()
        self.dx += 100
    else:
        self.dx += 100

  def up(self):
    if 21 <= self.y <= 65:
        self.dy -= 21
    elif self.y < 21:
        self.down()
        self.dy -= 100
    else:
        self.dy -= 100

  def down(self):
    if 621 >= self.y >= 590:
        self.dy += 21
    elif self.y > 621:
        self.up()
        self.dy += 100
    else:
        self.dy += 100

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25
    
  def reset(self):
    self.x = 0
    self.y = 0