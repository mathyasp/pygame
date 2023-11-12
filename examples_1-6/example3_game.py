# Example 3

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


# Make an instance of GameObject
apple = Apple()
strawberry = Strawberry()

# Create the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  # Clear screen
  screen.fill((255, 255, 255))
  
  # Draw apple
  apple.move()
  apple.render(screen)

  # Draw strawberry
  strawberry.move()
  strawberry.render(screen)
   
  
  # Update the window
  pygame.display.flip()
  # tick the clock!
  clock.tick(60)

