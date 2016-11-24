from Journal import Journal, db
from datetime import date
from PyQt5.QtCore import QTimer
import time

class JournalController():
    def __init__(self):
        db.connect()
        
        if not Journal.table_exists():
            Journal.create_table(True)
            
        self.create()
        

    def reset(self):
        self.create() 

    def create(self):
        try:
            self.journal = Journal.get(date = date.today())
        except Journal.DoesNotExist:
            self.journal = Journal.create(text = "", date = date.today())

    def update(self, text):
        self.journal.text = text
        self.journal.save()

    def get(self, date = date.today()):
        return Journal.get(date = date)
