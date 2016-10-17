# Module imports
import shelve
import time


# This is going to always return the current date for us
def curDate():
    return time.strftime("%m/%d/%Y")

class Journal():
    def __init__(self):
        self.journal = shelve.open("journal", writeback=True)

    def close(self):
        self.journal.close()


    def exists(self, date):
        if date in self.journal:
            return True
        
        return False

    def get(self, date = curDate()):
        if self.exists(date):
            return self.journal[date]

    def update(self, text):
        self.journal[curDate()] = text 
