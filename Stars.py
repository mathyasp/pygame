from random import choice
from GameObject import GameObject
from constants import *

class Star1(GameObject):
  def __init__(self):
    super(Star1, self).__init__(0, 0, 'images/Star1.png')
    self.dx = 0
    self.dy = speed
    self.reset() # call reset here! 

  def move(self):
    self.x += self.dx
    self.y += self.dy
   # Check the y position of the Star1
    if self.y > 670 or self.y < -70: 
      self.reset()

  # add a new method
  def reset(self):
    direction = choice(u_or_d)
    if direction == 'up':
      self.x = choice(lanes_x)
      self.y = 670
      self.dy = -speed
    else:
      self.x = choice(lanes_x)
      self.y = -70
      self.dy = speed


class Star2(GameObject):
  def __init__(self):
   super(Star2, self).__init__(0, 0, 'images/Star2.png')
   self.dy = 0
   self.dx = speed
   self.reset() # call reset here! 

  def move(self):
   self.y += self.dy
   self.x += self.dx
   # Check the y position of the Star2
   if self.x > 380 or self.x < -70: 
     self.reset()

  # add a new method
  def reset(self):
    direction = choice(l_or_r)
    if direction == 'left':
      self.y = choice(lanes_y)
      self.x = 380
      self.dx = -speed
    else:
      self.y = choice(lanes_y)
      self.x = -70
      self.dx = speed