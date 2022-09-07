# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

xa = int(input('enter the X coordinate of point A: '))
ya = int(input('enter the Y coordinate of point A: '))
xb = int(input('enter the X coordinate of point B: '))
yb = int(input('enter the Y coordinate of point B: '))
distance = (((xa - xb) ** 2 + (ya - yb) ** 2)**0.5)
print(f'A ({xa},{ya}); B ({xb},{yb}) -> {int(distance * 100) / 100}')
