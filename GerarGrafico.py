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
a= Teste.select(Teste.data).execute()
for x in a:
    print(x)
print(a.get())
# lista = [item for item in Teste.select().dicts()]
# for x in lista:
#     print(x)
