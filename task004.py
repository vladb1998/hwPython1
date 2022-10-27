numQuarter= int (input(' Введите номер четверти: '))
if ( numQuarter == 1):
    print(f' В {numQuarter} четверти: x = от 0 до + бесконечности ; y = 0 до + бесконечности ')
elif (numQuarter == 2):
    print(f' В {numQuarter} четверти: x = от 0 до - бесконечности ; y = 0 до + бесконечности ')
elif (numQuarter == 3):
    print(f' В {numQuarter} четверти: x = от 0 до - бесконечности ; y = 0 до - бесконечности ')
elif (numQuarter == 4):
    print(f' В {numQuarter} четверти: x = от 0 до + бесконечности ; y = 0 до - бесконечности ')
else: print(' Такой четверти не существует')