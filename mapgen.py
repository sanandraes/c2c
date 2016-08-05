import settings, map, random

SEEDS = 3000
GENERATIONS = 4


def generate(typeflag, emptymap):
	if typeflag == 'cellular':
		
		#seed the initial cells
		i = 0
		while(i < SEEDS):
			x = random.randint(0, emptymap.width-1)
			y = random.randint(0, emptymap.height-1)
			emptymap.maparray[x][y].terrain = map.grassland
			i += 1
			
		#run generations
		i = 0
		while(i < GENERATIONS):
			fliparray = [[0 for x in range(emptymap.width)] for y in range(emptymap.height)]
			
			for y in range(1,emptymap.height-1):
				for x in range(1,emptymap.width-1):
					if emptymap.maparray[x][y].terrain == map.ocean:
						count = 0
						
						for j in range(x-1, x+2):
							for k in range(y-1, y+2):
								if emptymap.maparray[j][k].terrain == map.grassland:
									count += 1
						
						if count == 4 or count == 5:
							fliparray[x][y] = 1
							
			for y in range(emptymap.height):
				for x in range(emptymap.width):
					if fliparray[x][y] == 1:
						emptymap.maparray[x][y].terrain = map.grassland
			i += 1