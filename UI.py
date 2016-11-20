# Module imports
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import date

# User imports
 
class Window(QMainWindow):
    # Set defaults
    width = 700
    height = 550
    title = "OpenJournal"
	
    def __init__(self, journal):
        super().__init__()
        
        self.JournalController = journal

        self.buildUI()

        self.startDateLoop()

    def checkDate(self):
        if self.JournalController.journal.date != date.today():
            self.JournalController.reset()
            self.updateDateLabel()
            self.textEditor.setPlainText(self.JournalController.journal.text)

    def startDateLoop(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.checkDate)
        self.timer.start(1)

    def buildUI(self):
        grid = QGridLayout()
        grid.setSpacing(0) 
        grid.setContentsMargins(2,2,2,2)
        self.setStyleSheet("background-color: white");

        self.textEditor = QPlainTextEdit(self)
        self.textEditor.setFrameStyle(QFrame.NoFrame);
        # Set the initial text
        self.textEditor.setPlainText(self.JournalController.journal.text)
    
        # Set the initial size and title
        self.initSize()
        self.setWindowTitle(self.title)

        dateLabelWidget = QWidget()
        dateLabelWidget.setFixedSize(125,self.height)

        self.dateLabel = QLabel(dateLabelWidget)
        self.dateLabel.setAlignment(Qt.AlignRight | Qt.AlignTop)
        self.updateDateLabel()


        widget = QWidget()
        grid.addWidget(self.textEditor, 0, 0)
        grid.addWidget(dateLabelWidget, 0, 1)
        widget.setLayout(grid) 

        self.setCentralWidget(widget)

        # Show our UI
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

    def showJournals(self):
        self.latestJournal = journal.get()
        self.viewDate = QLabel()
        self.viewDate.setText(self.latestJournal['date'])

    def updateDateLabel(self):
        self.dateLabel.setText(time.strftime("%B %d, %Y"))

    def keyReleaseEvent(self, event):
        text = str(self.textEditor.toPlainText())
        self.JournalController.update(text)
