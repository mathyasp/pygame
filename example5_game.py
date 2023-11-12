# Example 5

# Import and initialize pygame
from random import randint, choice
import pygame
pygame.init()

# Get the clock
clock = pygame.time.Clock()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# List of lane coordinates
lanes = [93, 218, 343]

# Left or right
l_or_r = ['left', 'right']

# Up or down
u_or_d = ['up', 'down']

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
    super(Apple, self).__init__(0, 0, 'apple.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.reset() # call reset here! 

  def move(self):
    self.x += self.dx
    self.y += self.dy
   # Check the y position of the apple
    if self.y > 505 or self.y < -65: 
      self.reset()

  # add a new method
  def reset(self):
    direction = choice(u_or_d)
    if direction == 'up':
      self.x = choice(lanes)
      self.y = 505
      self.dy = -((randint(0, 200) / 100) + 1)
    else:
      self.x = choice(lanes)
      self.y = -65
      self.dy = (randint(0, 200) / 100) + 1


class Strawberry(GameObject):
  def __init__(self):
   super(Strawberry, self).__init__(0, 0, 'strawberry.png')
   self.dy = 0
   self.dx = (randint(0, 200) / 100) + 1
   self.reset() # call reset here! 

  def move(self):
   self.y += self.dy
   self.x += self.dx
   # Check the y position of the strawberry
   if self.x > 505 or self.x < -65: 
     self.reset()

  # add a new method
  def reset(self):
    direction = choice(l_or_r)
    if direction == 'left':
      self.y = choice(lanes)
      self.x = 505
      self.dx = -((randint(0, 200) / 100) + 1)
    else:
      self.y = choice(lanes)
      self.x = -65
      self.dx = (randint(0, 200) / 100) + 1
      


class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'player.png')
    self.dx = 0
    self.dy = 0
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


class Bomb(GameObject):
  def __init__(self):
    super(Bomb, self).__init__(0, 0, 'bomb.png')
    self.dx = 0
    self.dy = 0
    self.reset() # call reset here! 

  def move(self):
    self.x += self.dx
    self.y += self.dy
   # Check the y position of the apple
    if self.y > 505 or self.y < -65: 
      self.reset()
    if self.x > 505 or self.x < -65: 
     self.reset()

  # add a new method
  def reset(self):
    direction_options = [choice(u_or_d), choice(l_or_r)]
    chosen_direction = choice(direction_options)
    if chosen_direction == 'up':
      self.x = choice(lanes)
      self.y = 505
      self.dy = -((randint(0, 200) / 100) + 1)
      self.dx = 0
    elif chosen_direction == 'down':
      self.x = choice(lanes)
      self.y = -65
      self.dy = (randint(0, 200) / 100) + 1
      self.dx = 0
    elif chosen_direction == 'left':
      self.y = choice(lanes)
      self.x = 505
      self.dx = -((randint(0, 200) / 100) + 1)
      self.dy = 0
    else:
      self.y = choice(lanes)
      self.x = -65
      self.dx = (randint(0, 200) / 100) + 1
      self.dy = 0

# Make an instance of GameObject
apple = Apple()
strawberry = Strawberry()

# make an instance of Player
player = Player()

# make an instance of Bomb
bomb = Bomb()

# Make a group
all_sprites = pygame.sprite.Group()

# Add sprites to group
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)

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

  # Move and render Sprites
  for entity in all_sprites:
    entity.move()
    entity.render(screen)

  # Update the window
  pygame.display.flip()

  # tick the clock!
  clock.tick(60)