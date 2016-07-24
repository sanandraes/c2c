import pygame, time, map
pygame.init()

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
TILE_SIZE = 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
image = pygame.image.load("image.bmp")
image_rect = image.get_rect()

def render_map(activemap):
	for x in range(activemap.width):
		for y in range(activemap.height):
			pygame.draw.rect(screen, activemap.maparray[x][y].terrain.color, (x*activemap.side_length, y*activemap.side_length, activemap.side_length, activemap.side_length))

testmap = map.Map(SCREEN_WIDTH/TILE_SIZE,SCREEN_HEIGHT/TILE_SIZE,TILE_SIZE)

while 1:
	render_map(testmap)
	pygame.display.flip()