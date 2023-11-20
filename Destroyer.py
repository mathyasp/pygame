from random import choice
from GameObject import GameObject
from constants import *

class Destroyer(GameObject):
  def __init__(self):
    super(Destroyer, self).__init__(0, 0, 'images/Destroyer.png')
    self.dx = speed
    self.dy = speed
    self.reset() # call reset here! 

  def move(self):
    self.x += self.dx
    self.y += self.dy
   # Check the y position of the Star1
    if self.y > 670 or self.y < -70: 
      self.reset()
    if self.x > 380 or self.x < -70: 
     self.reset()

  # add a new method
  def reset(self):
    direction_options = [choice(u_or_d), choice(l_or_r)]
    chosen_direction = choice(direction_options)
    if chosen_direction == 'up':
      self.x = choice(lanes_x)
      self.y = 670
      self.dy = -speed
      self.dx = 0
    elif chosen_direction == 'down':
      self.x = choice(lanes_x)
      self.y = -70
      self.dy = speed
      self.dx = 0
    elif chosen_direction == 'left':
      self.y = choice(lanes_y)
      self.x = 380
      self.dx = -speed
      self.dy = 0
    else:
      self.y = choice(lanes_y)
      self.x = -70
      self.dx = speed
      self.dy = 0
