import math
volume = float(input("Введите объём: "))
radius = (3*(volume**(1/3)))/(4* math.pi)
print("Радиус равен: ", radius)
