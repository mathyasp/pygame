from random import randint
from GameObject import GameObject

class Cloud1(GameObject):
  def __init__(self):
    super(Cloud1, self).__init__(0, 0, 'images/gascloud.png')
    self.dx = 0.3
    self.dy = 0
    self.reset() # call reset here! 

  def move(self):
    self.x += self.dx
    self.y += self.dy
   # Check the y position of the Cloud
    if self.x > 505 or self.x < -130: 
      self.reset()

  # add a new method
  def reset(self):
    direction = randint(0, 1)    
    if direction == 1:
      self.y = randint(0, 634)
      self.x = 376
      self.dx = -0.3
    else:
      self.y = randint(0, 634)
      self.x = -127
      self.dx = 0.3

class Cloud2(GameObject):
  def __init__(self):
    super(Cloud2, self).__init__(0, 0, 'images/gascloud.png')
    self.dx = 0.2
    self.dy = 0
    self.reset() # call reset here! 

  def move(self):
    self.x += self.dx
    self.y += self.dy
   # Check the y position of the Cloud
    if self.x > 505 or self.x < -130: 
      self.reset()

  # add a new method
  def reset(self):
    direction = randint(0, 1)    
    if direction == 1:
      self.y = randint(0, 634)
      self.x = 668
      self.dx = -0.2
    else:
      self.y = randint(0, 634)
      self.x = -127
      self.dx = 0.2

class Cloud3(GameObject):
  def __init__(self):
    super(Cloud3, self).__init__(0, 0, 'images/gascloud.png')
    self.dx = 0.1
    self.dy = 0
    self.reset() # call reset here! 

  def move(self):
    self.x += self.dx
    self.y += self.dy
   # Check the y position of the Cloud
    if self.x > 505 or self.x < -130: 
      self.reset()

  # add a new method
  def reset(self):
    direction = randint(0, 1)    
    if direction == 1:
      self.y = randint(0, 634)
      self.x = 668
      self.dx = -0.1
    else:
      self.y = randint(0, 634)
      self.x = -127
      self.dx = 0.1