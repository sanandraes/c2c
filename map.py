import pygame, random, settings, camera, mapgen

#def terrain, contains info about rendering to map and game mechanics
class Terrain:
	def __init__(self, colour):
		self.color = colour

#define some placeholder terrains for testing, eventually this should be part of an init somewhere
grassland = Terrain(pygame.Color('#6EA028'))
ocean = Terrain(pygame.Color('#0000cc'))

#a cell on a map, will contain a terrain object, and info about units/cities/cultures/workers whatever
class Tile:
	def __init__(self, terrain, explored = True):
		#add some idea of terrain, movement blocking, improvements, culture... ???
		self.explored = explored
		self.terrain = terrain

#map, contains an array of tiles and some infrastructure for rendering/viewporting
class Map:
	def __init__(self, width, height, side_length):
		#some important constants/values 
		self.width = width
		self.height = height
		self.side_length = side_length
		
		#generate a 'blank' array of tiles
		self.maparray = [[Tile(ocean) for y in range(height)] for x in range(width)]
		
		#init a camera
		self.camerarect = pygame.Rect((0,0),(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
		self.camera = camera.Camera(self.camerarect, (0,0), (self.width, self.height))
		
		#map generation
		mapgen.generate('cellular', self)
		
		#create important surface to hold graphical information
		self.mapsurface = pygame.Surface((side_length*width, side_length*height))
		
		#draw the mapsurface of which the viewport is a subset
		self.ready_surface()

	#creates a graphical interpretaion of self.maparray on self.mapsurface
	def ready_surface(self):
		for x in range(self.width):
			for y in range(self.height):
				pygame.draw.rect(self.mapsurface, self.maparray[x][y].terrain.color, (x*self.side_length, y*self.side_length, self.side_length, self.side_length))

	#send a subset of self.mapsurface (defined by self.camrerect) to a surface 'dest', (this is all but hardcoded as main.screen, that's probably bad...)
	def render(self, dest):
		dest.blit(self.mapsurface, (0,0), self.camera.camerarect)
