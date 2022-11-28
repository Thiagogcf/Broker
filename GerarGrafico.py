import datetime
import random
from time import strptime, mktime
from datetime import datetime

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

class Total(BaseModel):
    id = IntegerField()
    dado = IntegerField()
    data = DateTimeField()

for h in range(1,12):
    Teste.insert(dado=(random.randint(1,10)),data=(datetime(datetime.now().year, datetime.now().month, datetime.now().day,h))).execute()
a= Teste.select(Teste.data).execute()
lista = [item for item in Teste.select().dicts()]
dados=[]
datas = []
for x in lista:
    dados.append(x['dado'])
    datas.append(x['data'])
    Teste.insert(dado=x['dado'], data=x['data']).execute()

dates = matplotlib.dates.date2num(datas)
plt.plot(datas,dados)
plt.title(datetime.today())
plt.gcf().autofmt_xdate()

plt.show()
Teste.delete().execute()

