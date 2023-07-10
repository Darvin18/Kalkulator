import functions

while True:
    question = input('Что будем делать? +, -, *, /  ')
    if question == 'q':
        break
    first_number = float(input('Введите первое число: '))
    second_number = float(input('Введите второе число: '))

    if question == '+':
        f = functions.plus(first_number,second_number)
        print(f)
    elif question == '-':
        f = functions.minus(first_number, second_number)
        print(f)
    elif question == '*':
        f = functions.ymnojenie(first_number, second_number)
        print(f)
    elif question == '/':
        f = functions.delenie(first_number, second_number)
        print(f)

