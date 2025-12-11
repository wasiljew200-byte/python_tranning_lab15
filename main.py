from plasticToys import PlasticToys
from softToys import SoftToys

lego = PlasticToys("Лего", "Петя", "500г")
print(lego.info())
print(lego.play())
print(lego.createToys())

bear = SoftToys("Медвежонок", "Маша", "1кг ваты")
print(bear.info())
print(bear.play())
print(bear.createToys())