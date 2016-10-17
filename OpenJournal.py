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
import Shortcuts
from Journal import Journal

# Make sure this script isn't being imported
if __name__ == '__main__':
    OpenJournal = QApplication(sys.argv)

    # Load the journal class (this doesn't actually create a new journal)
    journal = Journal()

    # Create the window
    window = Window(journal)

    # Load shortcuts given our window
    Shortcuts.load(window)

    sys.exit(OpenJournal.exec_())
