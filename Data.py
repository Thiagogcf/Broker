from datetime import datetime
from peewee import (
    SqliteDatabase, Model, TextField, ForeignKeyField,
    DateTimeField, IntegerField
)


db = SqliteDatabase('notas.db')


class BaseModel(Model):
    class Meta:
        database = db


class Pessoa(BaseModel):
    tempo = IntegerField()




Pessoa.create_table()