import pygame, settings

class Camera:
	def __init__(self, camerarect, (vx, vy), (mapwidth, mapheight)):
		self.camerarect = camerarect
		self.camreavel = (vx, vy)
		self.mapwidth = mapwidth
		self.mapheight = mapheight
		
	#move the camera by dx and dy
	def move_camera(self, dx, dy):
		self.camerarect.left += dx
		self.camerarect.top += dy
		
		if self.camerarect.left < 0:
			self.camerarect.left = 0
		elif self.camerarect.left >= self.mapwidth*settings.TILE_SIZE - self.camerarect.width:
			self.camerarect.left = self.mapwidth*settings.TILE_SIZE - self.camerarect.width
		if self.camerarect.top < 0:
			self.camerarect.top = 0
		elif self.camerarect.top >= self.mapwidth*settings.TILE_SIZE - self.camerarect.height:
			self.camerarect.top = self.mapwidth*settings.TILE_SIZE - self.camerarect.height
	
	def set_vel(vx, vy):
		self.cameravel = (vx, vy)