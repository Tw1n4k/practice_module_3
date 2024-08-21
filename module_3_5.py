a = 1
while a != 0:
    def get_multiplied_digits(number):
        str_number = str(number)
        first = int(str_number[0])
        if len(str_number) > 1:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            return first


    a = get_multiplied_digits(int(input('Введите любое целое число:')))
    if a != 0:
        print(a)
        print('Для завершения программы введите 0')
    else:
        print('Работа программы завершена!')
