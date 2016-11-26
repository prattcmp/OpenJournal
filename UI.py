# Module imports
import sys
import time
import platform
import dateutil.parser
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from datetime import date

# User imports
 
class Window(QtWidgets.QMainWindow):
    # Set defaults
    width = 700
    height = 550
    title = "OpenJournal (alpha)"
	
    def __init__(self, journal):
        super().__init__()
        
        self.firstView = True
        self.JournalController = journal

        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+W"), self, self.closeProgram)
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+E"), self, self.changeView)

        self.buildUI()

        self.startDateLoop()

    def checkDate(self):
        if self.JournalController.journal.date != date.today():
            self.JournalController.reset()
            self.updateDateLabel()
            self.textEditor.setPlainText(self.JournalController.journal.text)

    def startDateLoop(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.checkDate)
        self.timer.start(1)

    def buildUI(self):
        # Create our pages (stacks)
        self.editStack = QtWidgets.QWidget()
        self.viewStack = QtWidgets.QWidget()
        self.editStackUI()
        self.viewStackUI()

        # Put them in a stack widget so we can rotate between them
        self.stack = QtWidgets.QStackedWidget(self)
        self.stack.addWidget(self.editStack)
        self.stack.addWidget(self.viewStack)
        self.setCentralWidget(self.stack)

        # Set the initial size and title
        self.initSize()
        self.setWindowTitle(self.title)

        # Show our UI
        self.show()

    def editStackUI(self):
        grid = QtWidgets.QGridLayout()
        grid.setSpacing(0) 
        grid.setContentsMargins(2,2,2,2)
        self.setStyleSheet("background-color: white");

        # Text editor widget
        self.textEditor = QtWidgets.QPlainTextEdit(self)
        self.textEditor.setFrameStyle(QtWidgets.QFrame.NoFrame);
        self.textEditor.setPlainText(self.JournalController.journal.text)

        # Directions widget
        self.instructLabel = QtWidgets.QLabel()
        self.instructLabel.setText("Press " + ("Cmd" if platform.system() == "Darwin" else "Ctrl") + "+E to view journals")
        self.instructLabel.setFixedHeight(18)
        self.instructLabel.setStyleSheet('color: gray')
        # Current date widget
        self.dateLabel = QtWidgets.QLabel()
        self.dateLabel.setFixedHeight(18)
        self.updateDateLabel()


        grid.addWidget(self.textEditor, 0, 0, 100, 1)
        grid.addWidget(self.instructLabel, 0, 1, 1, 1)
        grid.addWidget(self.dateLabel, 1, 1, 1, 1, QtCore.Qt.AlignRight)

        self.editStack.setLayout(grid)

    def viewStackUI(self):
        grid = QtWidgets.QGridLayout()
        grid.setSpacing(0) 
        grid.setContentsMargins(2,2,2,2)
        self.setStyleSheet("background-color: white");

        # Text viewer widget
        self.textViewer = QtWidgets.QPlainTextEdit(self)
        self.textViewer.setFrameStyle(QtWidgets.QFrame.NoFrame);

        self.textViewer.setReadOnly(True)

        # Directions widget
        self.instructLabel = QtWidgets.QLabel()
        self.instructLabel.setText("Press " + ("Cmd" if platform.system() == "Darwin" else "Ctrl") + "+E to edit your journal")
        self.instructLabel.setFixedHeight(18)
        self.instructLabel.setStyleSheet('color: gray')
        # Current date widget
        self.dateLabel = QtWidgets.QLabel()
        self.dateLabel.setFixedHeight(18)
        self.updateDateLabel()

        self.backButton = QtWidgets.QPushButton("<")
        self.backButton.clicked.connect(self.goBack)
        self.backButton.setFixedWidth(50)
        self.forwardButton = QtWidgets.QPushButton(">")
        self.forwardButton.clicked.connect(self.goForward)
        self.forwardButton.setFixedWidth(50)

        grid.addWidget(self.textViewer, 0, 0, 100, 1)
        grid.addWidget(self.instructLabel, 0, 1, 1, 2)
        grid.addWidget(self.dateLabel, 1, 1, 1, 2, QtCore.Qt.AlignRight)
        grid.addWidget(self.backButton, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        grid.addWidget(self.forwardButton, 2, 2, 1, 1, QtCore.Qt.AlignRight)

        self.viewStack.setLayout(grid)
		
    def initSize(self):
        # Get user's computer resolution to properly size the window
        screen = QtWidgets.QDesktopWidget().screenGeometry()

        # Make the window height 9/10th's of the screen height
        self.height = (8/10) * screen.height()
		
        # Get the coordinates for a centered window
        centeredX = (screen.width() / 2) - (self.width / 2)
        centeredY = (screen.height() / 2) - (self.height / 2)

        # Change height based on screen
        self.setGeometry(centeredX, centeredY, self.width, self.height)

    def updateDateLabel(self):
        self.dateLabel.setText(time.strftime("%B %d, %Y"))

    def goBack(self):
        journal = self.JournalController.back()

        if journal:
            self.textViewer.setPlainText(journal.text)
            self.dateLabel.setText(journal.date.strftime("%B %d, %Y"))

    def goForward(self):
        journal = self.JournalController.forward()

        if journal:
            self.textViewer.setPlainText(journal.text)
            self.dateLabel.setText(journal.date.strftime("%B %d, %Y"))

    def keyReleaseEvent(self, event):
        if self.stack.currentIndex() == 0:
            text = str(self.textEditor.toPlainText())
            self.JournalController.update(text)


    def closeProgram(self):
        QtWidgets.QApplication.quit() 

    def changeView(self):
        if self.stack.currentIndex() == 0:
            self.stack.setCurrentIndex(1)
            journal = self.JournalController.back()
            journal = self.JournalController.forward()
            if journal:
                self.textViewer.setPlainText(journal.text)
        elif self.stack.currentIndex() == 1:
            self.stack.setCurrentIndex(0)
