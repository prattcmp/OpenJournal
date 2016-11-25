from Journal import Journal, db
from datetime import date, timedelta
from PyQt5.QtCore import QTimer
import time

class JournalController():
    def __init__(self):
        self.viewDate = date.today()

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
        if self.viewDate == date.today():
            return False
        self.viewDate += timedelta(1)

        try:
            journals = Journal.select().where(Journal.date >= self.viewDate.isoformat()).order_by(Journal.date.asc())
            return journals[0]
        except IndexError:
            self.viewDate -= timedelta(1)

            return False

    def back(self):
        self.viewDate -= timedelta(1)

        try:
            journals = Journal.select().where(Journal.date <= self.viewDate.isoformat()).order_by(Journal.date.desc())
            return journals[0]
        except IndexError:
            self.viewDate += timedelta(1)

            return False

    def get(self, date = date.today()):
        return Journal.get(date = date)
