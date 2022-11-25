import random
from datetime import datetime

from peewee import (
    SqliteDatabase, Model, IntegerField,DateTimeField
)


db = SqliteDatabase('Banco.db')


class BaseModel(Model):
    class Meta:
        database = db


class Teste(BaseModel):
    id = IntegerField()
    dado = IntegerField()
    data = DateTimeField()




Teste.create_table()
for x in range(1000):
    Teste.insert(id=x,dado=random.randint(1,10),data=datetime.now()).execute()
    print(x)