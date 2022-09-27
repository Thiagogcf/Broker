from peewee import (
    SqliteDatabase, Model, IntegerField
)


db = SqliteDatabase('Banco.db')


class BaseModel(Model):
    class Meta:
        database = db


class Teste(BaseModel):
    dado = IntegerField()




Teste.create_table()