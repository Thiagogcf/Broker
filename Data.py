from peewee import SqliteDatabase, Model, CharField
db = SqliteDatabase('aulax.db')
class Pessoa(Model):
    valor1 = CharField()
    class Meta:
        DataBase = db

Pessoa.create()