import pygame

class Terrain:
	def __init__(self, colour):
		self.color = colour

grassland = Terrain(pygame.Color('#6EA028'))
		
class Tile:
	def __init__(self, terrain = grassland, explored = True):
		#add some idea of terrain, movement blocking, improvements, culture... ???
		self.explored = explored
		self.terrain = terrain

class Map:
	def __init__(self, width, height, side_length = 10):
		self.width = width
		self.height = height
		self.side_length = side_length
		self.maparray = [[Tile(grassland) for y in range(height)] for x in range(width)]
		

