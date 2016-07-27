import pygame, settings, time, map
from pygame.locals import * #to make namespace calls not suck
pygame.init()


screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

testmap = map.Map(100, 100, settings.TILE_SIZE)
testmap.ready_surface()

def handle_input():
	for event in pygame.event.get():
		if event.type == QUIT:
			quit()
	
	keyspressed = pygame.key.get_pressed()
	
	if keyspressed[K_DOWN]:
		testmap.move_camera(0,1)
	elif keyspressed[K_UP]:
		testmap.move_camera(0,-1)
	if keyspressed[K_LEFT]:
		testmap.move_camera(-1,0)
	elif keyspressed[K_RIGHT]:
		testmap.move_camera(1,0)
	
			
while 1:
	
	handle_input()
	testmap.render(screen)
	pygame.display.flip()
	
