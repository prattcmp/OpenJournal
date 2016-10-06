'''
Open Journal

Created 10/05/2016
Author: Christopher Pratt
'''

# Module imports
import sys
from PyQt5.QtWidgets import QApplication

# User imports
from UI import Window

# Make sure this script isn't being imported
if __name__ == '__main__':
	OpenJournal = QApplication(sys.argv)
	
	# Create the window
	w = Window()
	sys.exit(OpenJournal.exec_())