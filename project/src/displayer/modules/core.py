from modules.window import Window
import sys

class Core:
	_map = []

	def __init__(self):
		self.window = Window()

	def getMap(self):
		try:
			with open(self._map_path, 'r') as file:
				map = file.read().strip().split('\n')

				for line in map:
					self._map.append(line.split(','))
		except Exception as e:
			print '\033[31m%s\033[m' % (e)
			sys.exit(-1)

	def loadMap(self, map_path):
		self._map_path = map_path
		self.getMap()
		self.window.displayMap(self._map)