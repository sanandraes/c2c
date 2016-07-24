import pygame, time, map
pygame.init()

size = width, height = 600, 400
screen = pygame.display.set_mode(size)
image = pygame.image.load("image.bmp")
image_rect = image.get_rect()

while 1:
	screen.blit(image, image_rect)
	pygame.display.flip()