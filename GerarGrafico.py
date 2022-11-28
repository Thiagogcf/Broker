import datetime
from time import strptime, mktime

import matplotlib
from peewee import (
    SqliteDatabase, Model, IntegerField, DateTimeField
)
import matplotlib.pyplot as plt
db = SqliteDatabase('Banco.db')


class BaseModel(Model):
    class Meta:
        database = db


class Teste(BaseModel):
    id = IntegerField()
    dado = IntegerField()
    data = DateTimeField()
a= Teste.select(Teste.data).execute()
lista = [item for item in Teste.select().dicts()]
dados=[]
datas = []
for x in lista:
    dados.append(x['dado'])
    datas.append(x['data'])

dates = matplotlib.dates.date2num(datas)
plt.plot(datas,dados)
plt.title(datetime.datetime.today())
plt.gcf().autofmt_xdate()

plt.show()