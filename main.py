from machine import Pin
from time import sleep

button = Pin(32, Pin.IN)
led = Pin(2, Pin.OUT)

while True:
  if button.value() == True:
    print("Enviado")
  else:
    print("Não enviado")
  sleep(.01)