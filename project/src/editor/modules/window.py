from pygame.locals import *
import pygame
import math
import sys

TILE_WIDTH = 64
TILE_HEIGHT = 64

X_TILES = 3
Y_TILES = 3

WHITE = (255, 255, 255)
RED   = (255,   0,   0)

class Window:
	_map = []
	_map_path = ''
	_selected_tile = 0

	def displayGrid(self):
		for y in xrange(0, Y_TILES):
			for x in xrange(1, X_TILES):
				pygame.draw.aaline(self._display_surf, WHITE, (x * TILE_WIDTH, 0), (x * TILE_WIDTH, Y_TILES * TILE_HEIGHT), 0)
			pygame.draw.aaline(self._display_surf, WHITE, (0, y * TILE_HEIGHT), (X_TILES * TILE_WIDTH, y * TILE_HEIGHT), 0)

	def displaySelectionTiles(self):
		for x in xrange(0, Y_TILES):
			img = pygame.image.load('../../tiles/' + str(x) + '.png')
			self._display_surf.blit(img, (TILE_WIDTH * (X_TILES - 1), TILE_HEIGHT * x))

	def overlaySelectedTile(self):
		surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
		surface.set_alpha(128)
		surface.fill(RED)
		self._display_surf.blit(surface, (TILE_WIDTH * (X_TILES - 1), TILE_HEIGHT * self._selected_tile))

	def handleClick(self, mouse_pos):
		if mouse_pos[0] > (TILE_WIDTH * (X_TILES - 1)):
			self._selected_tile = int(math.floor(mouse_pos[1] / TILE_HEIGHT))
		else:
			x_index = int(math.floor(mouse_pos[0] / TILE_WIDTH))
			y_index = int(math.floor(mouse_pos[1] / TILE_HEIGHT))

			img = pygame.image.load('../../tiles/' + str(self._selected_tile) + '.png')

			self._display_surf.blit(img, (x_index * TILE_WIDTH, y_index * TILE_HEIGHT))
			self._map[y_index][x_index] = self._selected_tile

	def saveMap(self):
		try:
			file = open(self._map_path, 'w')

			for y in self._map:
				file.write(','.join(map(str, y)) + '\n')
		except Exception as e:
			print '\033[31m%s\033[m' % (e)
			sys.exit(-1)

	def displayEditor(self, map_path):
		self._map_path = map_path
		self._map = [[-1 for x in range(X_TILES - 1)] for y in range(Y_TILES)]
		self._running = True
		self._size = (TILE_WIDTH * X_TILES, TILE_HEIGHT * Y_TILES)
		self._display_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)

		pygame.display.set_caption('Editor')
		pygame.init()

		while self._running:
			self.displaySelectionTiles()
			self.displayGrid()
			self.overlaySelectedTile()

			try:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						self._running = False
					elif event.type == pygame.KEYDOWN:
						if event.key == 27:
							self._running = False
					elif event.type == pygame.MOUSEBUTTONUP:
						self.handleClick(pygame.mouse.get_pos())
				pygame.display.flip()
			except KeyboardInterrupt:
				self._running = False

		self.saveMap()
		pygame.quit()