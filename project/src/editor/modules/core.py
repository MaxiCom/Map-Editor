from modules.window import Window
import os.path
import sys

class Core:
	_map_path = ''

	def __init__(self):
		self.window = Window()

	def checkFile(self):
		if os.path.isfile(self._map_path):
			print '\033[31m%s already exists\033[m' % (self._map_path)
			sys.exit(-1)

	def loadEditor(self, map_path):
		self._map_path = map_path
		self.checkFile()
		self.window.displayEditor(map_path)