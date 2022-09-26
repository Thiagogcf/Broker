from peewee import (
    SqliteDatabase, Model, IntegerField
)


db = SqliteDatabase('notas.db')


class BaseModel(Model):
    class Meta:
        database = db


class Teste(BaseModel):
    dado = IntegerField()




Teste.create_table()