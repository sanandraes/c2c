import pygame, settings, time, map
from pygame.locals import * #to make namespace calls not suck
pygame.init()

#init screen
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

#init a map
testmap = map.Map(100, 100, settings.TILE_SIZE)

def handle_input():
	
	#if the player quit, then quit...
	for event in pygame.event.get():
		if event.type == QUIT:
			quit()
	
	#collect the current keyboard/mouse state
	keyspressed = pygame.key.get_pressed()
	mousepos = pygame.mouse.get_pos()
	
	#map arrow keys to camera movement
	if keyspressed[K_DOWN]:
		testmap.move_camera(0,1)
	elif keyspressed[K_UP]:
		testmap.move_camera(0,-1)
	if keyspressed[K_LEFT]:
		testmap.move_camera(-1,0)
	elif keyspressed[K_RIGHT]:
		testmap.move_camera(1,0)
		
	#edgepanning code, maybe tighten this up: diagonals are not friendly
	if mousepos[0] < 3:
		testmap.move_camera(-1,0)
	elif mousepos[0] > settings.SCREEN_WIDTH - 4:
		testmap.move_camera(1,0)
	if mousepos[1] < 3:
		testmap.move_camera(0,-1)
	elif mousepos[1] > settings.SCREEN_HEIGHT - 4:
		testmap.move_camera(0,1)
		
#game loop		
while 1:
	handle_input()
	testmap.render(screen)
	pygame.display.flip()
	
