corX = int (input(' Введите координаты точки X: '))
corY = int (input(' Введите координаты точки Y: '))
if (corX > 0 and corY > 0):
    print(f' Точка с координатами x: {corX} и y: {corY} находится в первой четверти')
elif (corX < 0 and corY > 0):
    print(f' Точка с координатами x: {corX} и y: {corY} находится в второй четверти')
elif (corX < 0 and corY < 0):
    print(f' Точка с координатами x: {corX} и y: {corY} находится в третьей четверти')
elif (corX > 0 and corY < 0):
    print(f' Точка с координатами x: {corX} и y: {corY} находится в четвертой четверти')
else: print("Такой точки не существует")