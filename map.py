import pygame, random, settings

#def terrain, contains info about rendering to map and game mechanics
class Terrain:
	def __init__(self, colour):
		self.color = colour

#define some placeholder terrains for testing, eventually this should be part of an init somewhere
grassland = Terrain(pygame.Color('#6EA028'))
ocean = Terrain(pygame.Color('#0000cc'))
		
#a placeholder map generation basically, to be called in map init
def terrain_randomizer():
	p = random.random()
	if p > 0.5: return grassland
	else: return ocean

#a cell on a map, will contain a terrain object, and info about units/cities/cultures/workers whatever
class Tile:
	def __init__(self, terrain, explored = True):
		#add some idea of terrain, movement blocking, improvements, culture... ???
		self.explored = explored
		self.terrain = terrain

#map, contains an array of tiles and some infrastructure for rendering/viewporting
class Map:
	def __init__(self, width, height, side_length = 10):
		#some important constants/values 
		self.width = width
		self.height = height
		self.side_length = side_length
		self.camera_x = 0
		self.camera_y = 0
		
		#placeholder map generation
		self.maparray = [[Tile(terrain_randomizer()) for y in range(height)] for x in range(width)]
		
		#create important surfaces for viewport and rendering
		self.mapsurface = pygame.Surface((side_length*width, side_length*height))
		self.camerarect = pygame.Rect((self.camera_x,self.camera_y),(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
		
		#draw the mapsurface of which the viewport is a subset
		self.ready_surface()

	#creates a graphical interpretaion of self.maparray on self.mapsurface
	def ready_surface(self):
		for x in range(self.width):
			for y in range(self.height):
				pygame.draw.rect(self.mapsurface, self.maparray[x][y].terrain.color, (x*self.side_length, y*self.side_length, self.side_length, self.side_length))

	#send a subset of self.mapsurface (defined by self.camrerect) to a surface 'dest', (this is all but hardcoded as main.screen, that's probably bad...)
	def render(self, dest):
		dest.blit(self.mapsurface, (0,0), self.camerarect)
		
	#move the camera by dx and dy unless at an edge
	#this sounds inefficient to me, think about asigning direclty instead of through a variable
	def move_camera(self, dx, dy):
		self.camera_x += dx
		self.camera_y += dy
		
		if self.camera_x < 0:
			self.camera_x = 0;
		elif self.camera_x >= self.width*self.side_length - self.camerarect.width:
			self.camera_x = self.width*self.side_length - self.camerarect.width
			
		if self.camera_y < 0:
			self.camera_y = 0;
		elif self.camera_y >= self.height*self.side_length - self.camerarect.height:
			self.camera_y = self.height*self.side_length - self.camerarect.height
			
		
		self.camerarect.left = self.camera_x
		self.camerarect.top = self.camera_y
