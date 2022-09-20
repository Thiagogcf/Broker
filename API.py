import random

from Data import Teste
valor = random.randint(1,6)
print(valor)
t1 = Teste(
    dado=valor
)
t1.save()