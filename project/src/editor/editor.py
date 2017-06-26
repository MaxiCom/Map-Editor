#!/usr/bin/python2.7
from modules.core import Core
import sys

def main():
	core = Core()

	if len(sys.argv) == 2:
		core.loadEditor(sys.argv[1])	
	else:
		print '\033[31mUsage: ./editor.py new_map\033[m'

if __name__ == '__main__':
	main()