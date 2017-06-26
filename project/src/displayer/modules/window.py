from pygame.locals import *
import pygame
import sys

class Window:
	def populateMap(self, map):
		try:
			for i1, y in enumerate(map):
				for i2, x in enumerate(y):
					if x != '-1':
						img = pygame.image.load('../../tiles/' + x + '.png')
						self._display_surf.blit(img, (i2 * 64, i1 * 64))
		except Exception as e:
			print '\033[31m%s\033[m' % (e)
			sys.exit(-1)

	def displayMap(self, map):
		self._running = True
		self._size = (len(max(map, key=len) * 64), len(map) * 64)
		self._display_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self.populateMap(map);
		
		pygame.display.set_caption('Displayer')
		pygame.init()

		while self._running:
			try:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						self._running = False
					elif event.type == pygame.KEYDOWN:
						if event.key == 27:
							self._running = False
				pygame.display.flip()
			except KeyboardInterrupt:
				self._running = False

		pygame.quit()