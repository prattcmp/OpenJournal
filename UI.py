# Module imports
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget

class Window(QWidget):
	# Set defaults
	width = 650
	height = 550
	title = "OpenJournal"
	
	def __init__(self):
		super().__init__()
		
		self.buildUI()
		
	def buildUI(self):
		self.initSize()
		self.setWindowTitle(self.title)

		self.show()
		
	def initSize(self):
		# Get user's computer resolution to properly size the window
		screen = QDesktopWidget().screenGeometry()
		
		# Make the window height 9/10th's of the screen height
		self.height = (8/10) * resolution.height()
		
		# Get the coordinates for a centered window
		centeredX = (screen.width() / 2) - (self.width / 2)
		centeredY = (screen.height() / 2) - (self.height / 2)
		
		# Change height based on screen
		self.setGeometry(centeredX, centeredY, self.width, self.height)