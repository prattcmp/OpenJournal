# Module imports
import sys
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QPlainTextEdit

# User imports

class Window(QMainWindow):
    # Set defaults
    width = 700
    height = 550
    title = "OpenJournal"
	
    def __init__(self, journal):
        super().__init__()
        
        self.journal = journal

        self.buildUI()

    def buildUI(self):
        self.textEditor = QPlainTextEdit(self)

        # Set the initial text
        self.textEditor.setPlainText(self.journal.get())
        self.setCentralWidget(self.textEditor)
    	
        self.initSize()
        self.setWindowTitle(self.title)

        self.show()
		
    def initSize(self):
        # Get user's computer resolution to properly size the window
        screen = QDesktopWidget().screenGeometry()

        # Make the window height 9/10th's of the screen height
        self.height = (8/10) * screen.height()
		
        # Get the coordinates for a centered window
        centeredX = (screen.width() / 2) - (self.width / 2)
        centeredY = (screen.height() / 2) - (self.height / 2)

        # Change height based on screen
        self.setGeometry(centeredX, centeredY, self.width, self.height)

    def setDateLabel(self):
        pass

    def keyReleaseEvent(self, event):
        text = str(self.textEditor.toPlainText())
        self.journal.update(text)

    def closeEvent(self, event):
        self.journal.close()

        super(Window, self).closeEvent(event)
