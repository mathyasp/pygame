from GameObject import GameObject

class Supernova(GameObject):
  def __init__(self):
    super(Supernova, self).__init__(0, 0, 'images/Supernova.png')
    self.x = 124
    self.y = 286