from math import sqrt
Ax = int (input(' Введите координаты точки X1: '))
Ay = int (input(' Введите координаты точки Y1: '))
Bx = int (input(' Введите координаты точки X2: '))
By = int (input(' Введите координаты точки Y2: '))

print ( round (sqrt(pow(Bx - Ax , 2) + pow (By - Ay , 2)),3))