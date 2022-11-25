from peewee import (
    SqliteDatabase, Model, IntegerField, DateTimeField
)

db = SqliteDatabase('Banco.db')


class BaseModel(Model):
    class Meta:
        database = db


class Teste(BaseModel):
    id = IntegerField()
    dado = IntegerField()
    data = DateTimeField()

lista = [item for item in Teste.select().dicts()]
for x in lista:
    print(x)
