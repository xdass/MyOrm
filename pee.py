from peewee import *


db = SqliteDatabase('test_db')


class Person(Model):
    le = IntegerField()
    name = CharField()

    class Meta:
        database = db


db.connect()
db.create_tables([Person])

chel = Person(le='asdad', name='lOLEEEE')
print(chel.le)