# Module imports
from PyQt5.QtCore import QStandardPaths
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
from datetime import date

db = SqliteExtDatabase(str(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)) + "/OpenJournal.db")

class BaseModel(Model):
    class Meta:
        database = db

class Journal(BaseModel):
    text = TextField()
    date = DateField()

