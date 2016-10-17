# Module imports
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def load(window):
    QShortcut(QKeySequence("Ctrl+W"), window, closeProgram)
    QShortcut(QKeySequence("Ctrl+E"), window, showEntries)

def closeProgram():
    QApplication.quit() 

def showEntries():
    #FIXME: We want to call some method that will show all our entries
    pass
