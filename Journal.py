# Module imports
import os
from PyQt5 import QtCore
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
from datetime import date

dbDirectory = str(QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.AppDataLocation)) + "/OpenJournal"

if not os.path.exists(dbDirectory):
    os.makedirs(dbDirectory)
    
db = SqliteExtDatabase(dbDirectory + "/OpenJournal.db")

class BaseModel(Model):
    class Meta:
        database = db

class Journal(BaseModel):
    text = TextField()
    date = DateField()

