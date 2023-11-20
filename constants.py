import pygame

# Background image
bg = pygame.image.load('images/background.jpg')

# List of lane coordinates
lanes_x = [61, 186, 311]
lanes_y = [82, 228, 392, 556]

# Left or right
l_or_r = ['left', 'right']

# Up or down
u_or_d = ['up', 'down']

# speed of objects
speed = 2

# Collision counter
collisions = 0