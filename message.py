from database import DataBase
from datetime import datetime


class Message:
    def __init__(self):
        database = DataBase()
        self.databse = database

    def send(self, content, author):
        time = datetime.now().strftime("%H:%M:%S")
        self.databse.write(content, author, time)

    def get(self):
        return self.databse.read_all()
