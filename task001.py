numDay = int(input('Введите день недели '))
if (numDay == 1):
    print('Понедельник - это первый рабочий день недели')
elif(numDay == 2):
    print('Вторник - это второй рабочий день недели')
elif(numDay == 3):
    print('Среда- это третий рабочий день недели')
elif (numDay == 4):
    print(' Четверг - это четвертый день недели')
elif(numDay == 5):
    print(' Пятница -это последний рабочий день недели')
elif(numDay == 6):
    print(' Суббота - выходной')
elif (numDay == 7):
    print(' Воскресенье - выходной')
else : print(' Такого дня не существует')