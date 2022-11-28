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
class Total(BaseModel):
    id = IntegerField()
    dado = IntegerField()
    data = DateTimeField()




Teste.create_table()
Total.create_table()
for x in range(2):
    Teste.insert(dado=random.randint(1,10),data=datetime.now()).execute()
    print(x)