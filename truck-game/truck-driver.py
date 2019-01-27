import pygame
import numpy as np
import json

WIDTH = 1230
HEIGHT = 758
TRUCK_ID = 11235
MAP_TOP_LEFT_LAT = 43.622159
MAP_TOP_LEFT_LONG = -79.710960
MAP_BOTTOM_RIGHT_LAT = 43.582567
MAP_BOTTOM_RIGHT_LONG = -79.615173
LAT_PX = abs(MAP_TOP_LEFT_LAT - MAP_BOTTOM_RIGHT_LAT) / HEIGHT
LONG_PX = abs(MAP_TOP_LEFT_LONG - MAP_BOTTOM_RIGHT_LONG) / WIDTH

def write_point_to_file(point):
	file = open('../truck_info.json', 'a')
	data = {
		'truck_id': TRUCK_ID,
		'latitude': point[0],
		'longitude': point[1]
	}
	file.write(json.dumps(data))
	file.write("\n")
	file.close()

def pixel2deg(point):
	point_deg = []
	point_deg = point_deg + [MAP_TOP_LEFT_LAT - point[1] * LAT_PX]
	point_deg = point_deg + [point[0] * LONG_PX + MAP_TOP_LEFT_LONG]
	return tuple(point_deg)

def deg2pixel(point):
	point_px = []
	point_px = point_px + [int(((point[1] - MAP_TOP_LEFT_LONG) / LONG_PX))]
	point_px = point_px + [int(((MAP_TOP_LEFT_LAT - point[0]) / LAT_PX))]
	return point_px

def plotPoints(screen):
	data = np.load('../directions/test.npy')
	pts = []
	for point in data:
		# point = data[i]
		# last_point = data[i - 1]
		#print(str(int(((point[1] - MAP_TOP_LEFT_LONG) / LONG_PX))), str(int(((MAP_TOP_LEFT_LAT - point[0]) / LAT_PX))))
		# pygame.draw.circle(screen, (255, 0, 255), (int(((point[1] - MAP_TOP_LEFT_LONG) / LONG_PX)), int(((MAP_TOP_LEFT_LAT - point[0]) / LAT_PX))), 3, 0)
		# pygame.draw.circle(screen, (255, 0, 255), deg2pixel(point), 3, 0)
		pts.append(deg2pixel(point))

	pygame.draw.lines(screen, (69, 69, 255), False, pts, 4)


def main():
	pygame.init()
	pygame.display.set_caption('Truck Driver Simulator')
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	bg = pygame.image.load("map_bg.png")
	bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
	truck = pygame.image.load('truck_sprite.png')
	truck = pygame.transform.scale(truck, (60, 60))

	print("Lat PX:", LAT_PX)
	print('Long Px:', LONG_PX)
	
	running = True
	x = 30
	y = 40
	size = 3
	step = 3
	loop_counter = 0

	while running:
		pygame.time.Clock().tick(30)
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
		plotPoints(screen)
		screen.blit(truck, (x-30, y-40))
		#pygame.draw.rect(screen, (255, 0, 0), (x, y, size, size), 1)
		pygame.draw.circle(screen, (255, 0, 0), (x, y), size, 0)
		
		if loop_counter == 30:
			print(str(x * LONG_PX + MAP_TOP_LEFT_LONG) + ', ' + str(MAP_TOP_LEFT_LAT - y * LAT_PX))
			pt = pixel2deg((x,y))
			write_point_to_file(pt)
			loop_counter = 0
		else:
			loop_counter += 1
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False


if __name__ == '__main__':
	main()
