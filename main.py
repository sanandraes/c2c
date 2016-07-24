import pygame, time
pygame.init()

size = width, height = 600, 400
screen = pygame.display.set_mode(size)
image = pygame.image.load("image.bmp")
image_rect = image.get_rect()

screen.blit(image, image_rect)
pygame.display.flip()

time.sleep(10)