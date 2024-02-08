from datetime import date

f = open(f'{date.today()}.txt', "w")
try:
    print("Введите список покупок:")
    while True:
        todo = input()
        if todo.lower() == 'стоп':
            break
        f.write(todo + '\n')
finally:
    f.close()