import pygame, random, settings

class Terrain:
	def __init__(self, colour):
		self.color = colour

grassland = Terrain(pygame.Color('#6EA028'))
ocean = Terrain(pygame.Color('#0000cc'))
		
def terrain_randomizer():
	p = random.random()
	if p > 0.5: return grassland
	else: return ocean
		
class Tile:
	def __init__(self, terrain, explored = True):
		#add some idea of terrain, movement blocking, improvements, culture... ???
		self.explored = explored
		self.terrain = terrain

class Map:
	def __init__(self, width, height, side_length = 10):
		self.width = width
		self.height = height
		self.side_length = side_length
		self.camera_x = 0
		self.camera_y = 0
		
		#placeholder map generation
		self.maparray = [[Tile(terrain_randomizer()) for y in range(height)] for x in range(width)]
		
		self.mapsurface = pygame.Surface((side_length*width, side_length*height))
		self.camerarect = pygame.Rect((self.camera_x,self.camera_y),(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
		
	def ready_surface(self):
		for x in range(self.width):
			for y in range(self.height):
				pygame.draw.rect(self.mapsurface, self.maparray[x][y].terrain.color, (x*self.side_length, y*self.side_length, self.side_length, self.side_length))

		
	def render(self, dest):
		dest.blit(self.mapsurface, (0,0), self.camerarect)
		
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
