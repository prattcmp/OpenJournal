from Journal import Journal, db
from datetime import date, timedelta
from PyQt5.QtCore import QTimer
import time

class JournalController():
    def __init__(self):
        self.viewID = Journal.get(date = date.today()).id

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

    def forward(self):
        try:
            journals = Journal.select().where(Journal.id > self.viewID).order_by(Journal.date.asc())
            self.viewID = journals[0].id

            return journals[0]
        except IndexError:
            return False

    def back(self):
        try:
            journals = Journal.select().where(Journal.id < self.viewID).order_by(Journal.date.desc())
            self.viewID = journals[0].id

            return journals[0]
        except IndexError:
            return False

    def get(self, date = date.today()):
        return Journal.get(date = date)
