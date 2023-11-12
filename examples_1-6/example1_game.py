# Import and initialize pygame
import pygame 
pygame.init()


# Configure the screen
screen = pygame.display.set_mode([500, 500])


""" Challenge 1 """
# Creat the game loop
# running = True 
# while running: 
# 	# Looks at events 
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			running = False
	
# 	# Clear the screen
# 	screen.fill((255, 255, 255))

# 	# Draw a circle
# 	red = (255, 0, 0)
# 	red_pos = (75, 75)
# 	pygame.draw.circle(screen, red, red_pos, 75)

# 	# Draw another circle
# 	orange = (255, 128, 0)
# 	orange_pos = (425, 75)
# 	pygame.draw.circle(screen, orange, orange_pos, 75)
	
# 	# Draw another circle
# 	yellow = (255, 255, 0)
# 	yellow_pos = (250, 250)
# 	pygame.draw.circle(screen, yellow, yellow_pos, 75)

# 	# Draw another circle
# 	green = (0, 255, 0)
# 	green_pos = (75, 425)
# 	pygame.draw.circle(screen, green, green_pos, 75)

# 	# Draw another circle
# 	blue = (51, 153, 255)
# 	blue_pos = (425, 425)
# 	pygame.draw.circle(screen, blue, blue_pos, 75)

# 	# Update the display
# 	pygame.display.flip()


""" Challenge 2 """
# Create the game loop
running = True 
while running: 
	# Looks at events 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	# Clear the screen
	screen.fill((255, 255, 255))

	# Calculate the radius of the circles based on the size of the screen
	radius = min(screen.get_width(), screen.get_height()) // 8

	# Calculate the distance between the centers of the circles based on the radius
	distance = radius * 3

	# Loop within a loop. The first loop counts the three rows. 
	# Within that loop add another loop that counts three columns.
	for x in range(3):
		for y in range(3):
			# Calculate the x and y coordinates of the center of the circle
			center_x = radius + (distance * x)
			center_y = radius + (distance * y)

			# Draw a circle
			color = (100, 100, 100)
			pygame.draw.circle(screen, color, (center_x, center_y), radius)

	# Update the display
	pygame.display.flip()