# Example 4

# Import and initialize pygame
from random import randint, choice
import pygame
pygame.init()

# Get the clock
clock = pygame.time.Clock()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# Game Object
class GameObject(pygame.sprite.Sprite):
  # Remove width and height and add image here!
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    # self.surf = pygame.Surface((width, height)) REMOVE!
    # self.surf.fill((255, 0, 255)) REMOVE!
    self.surf = pygame.image.load(image) # ADD!
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))


class Apple(GameObject):
 def __init__(self):
   super(Apple, self).__init__(0, 0, 'images/apple.png')
   self.dx = 0
   self.dy = (randint(0, 200) / 100) + 1
   self.reset() # call reset here! 

 def move(self):
   self.x += self.dx
   self.y += self.dy
   # Check the y position of the apple
   if self.y > 500: 
     self.reset()

 # add a new method
 def reset(self):
   self.x = choice([93, 218, 343])
   self.y = -64


class Strawberry(GameObject):
 def __init__(self):
   super(Strawberry, self).__init__(0, 0, 'images/stawberry.png')
   self.dy = 0
   self.dx = (randint(0, 200) / 100) + 1
   self.reset() # call reset here! 

 def move(self):
   self.y += self.dy
   self.x += self.dx
   # Check the y position of the strawberry
   if self.x > 500: 
     self.reset()

 # add a new method
 def reset(self):
   self.y = choice([93, 218, 343])
   self.x = -64


class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'images/player.png')
    self.dx = choice([93, 218, 343])
    self.dy = choice([93, 218, 343])
    self.reset()

  def left(self):
    if self.x <= 93:
        self.right()
    else:
        self.dx -= 125

  def right(self):
    if self.x >= 343:
        self.left()
    else:
        self.dx += 125

  def up(self):
    if self.y <= 93:
        self.down()
    else:
        self.dy -= 125

  def down(self):
    if self.y >= 343:
        self.up()
    else:
        self.dy += 125

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = 250 - 32
    self.y = 250 - 32


# Make an instance of GameObject
apple = Apple()
strawberry = Strawberry()

# make an instance of Player
player = Player()

# Create the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()
  
  # Clear screen
  screen.fill((255, 255, 255))
  
    # Draw apple
  apple.move()
  apple.render(screen)

  # Draw player 
  player.move()
  player.render(screen)

  # Draw strawberry
  strawberry.move()
  strawberry.render(screen)
   
  
  # Update the window
  pygame.display.flip()
  # tick the clock!
  clock.tick(60)