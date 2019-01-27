import pygame

WIDTH = 1230
HEIGHT = 758

def main():
	pygame.init()
	pygame.display.set_caption('Truck Driver Simulator')
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	bg = pygame.image.load("map_bg.png")
	pygame.transform.scale(bg, (WIDTH, HEIGHT))
	truck = pygame.image.load('truck_sprite.jpg')
	
	
	running = True
	x = 0
	y = 0
	size = 10
	step = 7
	loop_counter = 0

	while running:
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			y = max(0, y - step)
		if keys[pygame.K_DOWN]:
			y = min(HEIGHT-size, y + step)
		if keys[pygame.K_RIGHT]:
			x = min(WIDTH - size, x + step)
		if keys[pygame.K_LEFT]:
			x = max(0, x - step)

		screen.fill((0, 0, 0))
		screen.blit(bg, (0,0))
		screen.blit(truck, (x, y))
		#pygame.draw.rect(screen, (255, 0, 0), (x, y, size, size), 1)
		if loop_counter == 100:
			print(str(x) + ', ' + str(y))
			loop_counter = 0
		else:
			loop_counter += 1
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False


if __name__ == '__main__':
	main()