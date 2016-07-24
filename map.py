import pygame

class Terrain:
	def __init__(self, colour):
		self.color = colour

class Tile:
	def __init__(self, terrain, explored = True):
		#add some idea of terrain, movement blocking, improvements, culture... ???
		self.explored = explored
		self.terrain = terrain

class Map:
	def __init__(self, height, width):
		map = [[Tile() for y in range(height)] for x in range(width)]
		
grassland = Terrain(pygame.Color('#6EA028'))