# Example 2

# Import and initialize pygame
import pygame
pygame.init()
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

# Make an instance of GameObject
# box = GameObject(120, 300, 50, 50) REMOVE!
apple = GameObject(5, 5, 'images/apple.png')
apple2 = GameObject(430, 5, 'images/apple.png')
apple3 = GameObject(220, 220, 'images/apple.png')
apple4 = GameObject(5, 430, 'images/apple.png') 
apple5 = GameObject(430, 430, 'images/apple.png')
strawberry = GameObject(220, 5, 'images/stawberry.png')
strawberry2 = GameObject(5, 220, 'images/stawberry.png')
strawberry3 = GameObject(430, 220, 'images/stawberry.png')
strawberry4 = GameObject(220, 430, 'images/stawberry.png')

# Create the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  # Clear screen
  screen.fill((255, 255, 255))
  # box.render(screen) REMOVE!
  apple.render(screen) # ADD!
  strawberry.render(screen)
  apple2.render(screen)
  strawberry2.render(screen) 
  apple3.render(screen)
  strawberry3.render(screen)
  apple4.render(screen) 
  strawberry4.render(screen) 
  apple5.render(screen)
   
  
  # Update the window
  pygame.display.flip()

