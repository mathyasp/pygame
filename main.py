# Import and initialize pygame
import pygame
from GameObject import GameObject
from Clouds import Cloud1, Cloud2, Cloud3
from Stars import Star1, Star2
from Destroyer import Destroyer
from Supernova import Supernova
from Player import Player
from constants import *
pygame.init()

# Get the clock
clock = pygame.time.Clock()

# Configure the screen
screen = pygame.display.set_mode([375, 667])

# Make an instance of GameObjects
cloud1 = Cloud1()
cloud2 = Cloud2()
cloud3 = Cloud3()
star1 = Star1()
star2 = Star2()

# Make an instance of Player
player = Player()

# Make an instance of Destroyer
destroyer = Destroyer()

# Make an instance of Supernova
supernova = Supernova()

# Make a group
all_sprites = pygame.sprite.Group()

# Add sprites to group

all_sprites.add(player)
all_sprites.add(star1)
all_sprites.add(star2)
all_sprites.add(destroyer)
all_sprites.add(cloud1)
all_sprites.add(cloud2)
all_sprites.add(cloud3)

# make a stars Group
stars_sprites = pygame.sprite.Group()

# Add starss to stars_sprites
stars_sprites.add(star1)
stars_sprites.add(star2)

# Function to reset the game
def game_reset():
    # Clear screen
  screen.fill((255, 255, 255))

  screen.blit(bg, (0,0))

  # Move and render Sprites
  for entity in all_sprites:
    entity.move()
    entity.render(screen)


# Create the game loop
running = True
game_start = True
game_end = False

# Move the event handling code inside the game loop
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if game_start and event.key == pygame.K_RETURN:
        game_start = False
      elif not game_start:
        if event.key == pygame.K_ESCAPE:
          running = False
        elif event.key == pygame.K_q:
          running = False
        elif event.key == pygame.K_SPACE:
          if game_end:
            game_start = True
            game_end = False
            game_reset()
        elif not game_end:
          if event.key == pygame.K_LEFT:
            player.left()
          elif event.key == pygame.K_RIGHT:
            player.right()
          elif event.key == pygame.K_UP:
            player.up()
          elif event.key == pygame.K_DOWN:
            player.down()
      elif event.key == pygame.K_q:
        sys.exit()


  if game_start:
    screen.fill((255, 255, 255))
    start_game_message = pygame.font.Font(None, 36).render("Welcome to Mathyas' Game", True, (100, 0, 0))
    instruction_message = pygame.font.Font(None, 36).render("Avoid the obstacles!", True, (100, 0, 0))
    obstacle_message = pygame.font.Font(None, 36).render("If you hit 5 stars", True, (100, 0, 0))
    destroyer_message = pygame.font.Font(None, 36).render("Or hit the destroyer", True, (100, 0, 0))
    lose_message = pygame.font.Font(None, 36).render("You lose!", True, (100, 0, 0))
    ready_message = pygame.font.Font(None, 36).render("Press Enter to start!", True, (100, 0, 0))

    # Calculate x-coordinate for each message
    start_game_x = (375 - start_game_message.get_width()) // 2
    instruction_x = (375 - instruction_message.get_width()) // 2
    obstacle_x = (375 - obstacle_message.get_width()) // 2
    destroyer_x = (375 - destroyer_message.get_width()) // 2
    lose_x = (375 - lose_message.get_width()) // 2
    ready_x = (375 - ready_message.get_width()) // 2

    # Calculate y-coordinate for each message
    screen_height = screen.get_height()
    message_height = start_game_message.get_height()
    start_game_y = (screen_height - message_height * 6) // 2
    instruction_y = start_game_y + message_height
    obstacle_y = start_game_y + message_height * 2
    destroyer_y = start_game_y + message_height * 3
    lose_y = start_game_y + message_height * 4
    ready_y = start_game_y + message_height * 5

    screen.blit(start_game_message, (start_game_x, start_game_y))
    screen.blit(instruction_message, (instruction_x, instruction_y))
    screen.blit(obstacle_message, (obstacle_x, obstacle_y))
    screen.blit(destroyer_message, (destroyer_x, destroyer_y))
    screen.blit(lose_message, (lose_x, lose_y))
    screen.blit(ready_message, (ready_x, ready_y))

  else:
    game_reset()
    
    # Check Colisions
    stars = pygame.sprite.spritecollideany(player, stars_sprites)
    if stars:
      stars.reset()
      speed += 0.5
      collisions += 1

    # Check collision player and Destroyer
    if not game_end:
      if collisions == 5:
        game_end = True


      if pygame.sprite.collide_rect(player, destroyer):
        destroyer.reset()
        game_end = True

    if game_end:
      end_game_message = pygame.font.Font(None, 36).render("Game Over! You Lost.", True, (100, 0, 0))
      quit_message = pygame.font.Font(None, 36).render("Press Q if you give up.", True, (100, 0, 0)) 
      try_again_message = pygame.font.Font(None, 36).render("Press Space to try again.", True, (100, 0, 0)) 

      # Calculate x-coordinate for each message
      end_game_x = (screen.get_width() - end_game_message.get_width()) // 2
      quit_x = (screen.get_width() - quit_message.get_width()) // 2
      try_again_x = (screen.get_width() - try_again_message.get_width()) // 2

      # Calculate y-coordinate for each message
      end_game_y = (supernova.rect.y - end_game_message.get_height() * 3) // 2
      quit_y = end_game_y + end_game_message.get_height()
      try_again_y = quit_y + quit_message.get_height()

      screen.fill((255, 255, 255))
      supernova.render(screen)
      screen.blit(end_game_message, (end_game_x, end_game_y))
      screen.blit(quit_message, (quit_x, quit_y))
      screen.blit(try_again_message, (try_again_x, try_again_y))
      

  # Update the window
  pygame.display.flip()

  # tick the clock!
  clock.tick(60)