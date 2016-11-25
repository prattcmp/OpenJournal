'''
Open Journal

Created 10/05/2016
Author: Christopher Pratt
'''

# Module imports
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

# User imports
from UI import Window
import Shortcuts
from JournalController import JournalController

# Make sure this script isn't being imported
if __name__ == '__main__':
    OpenJournal = QtWidgets.QApplication(sys.argv)
    OpenJournal.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)

    # Load the journal class (this doesn't actually create a new journal)
    journal = JournalController()

    # Create the window
    window = Window(journal)

    sys.exit(OpenJournal.exec_())
