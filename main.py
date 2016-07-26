import pygame, settings, time, map
from pygame.locals import * #to make namespace calls not suck
pygame.init()


screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

testmap = map.Map(100, 100, settings.TILE_SIZE)
testmap.ready_surface()

def handle_input():
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
				testmap.move_camera(0,settings.TILE_SIZE)
			elif event.key == K_UP:
				testmap.move_camera(0,-settings.TILE_SIZE)
			elif event.key == K_LEFT:
				testmap.move_camera(-settings.TILE_SIZE,0)
			elif event.key == K_RIGHT:
				testmap.move_camera(settings.TILE_SIZE,0)
		elif event.type == QUIT:
			quit()
			
while 1:
	
	handle_input()
	testmap.render(screen)
	pygame.display.flip()
	
