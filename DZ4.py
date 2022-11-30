# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) 
# -2 -1 0 1 2 Позиции: 0,1 -> 2

def InputNumbers(inputText):
    oks = False
    while not oks:
        try:
            number = int(input(f"{inputText}"))
            oks = True
        except ValueError:
            print("Это не число!")
    return number

def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)

num = InputNumbers("Введите размер списка: ")
for e in range(- num, num + 1):
    list.append(mult(e))
print(f"Произведения чисел от {-num} до {num}:  {list}")

#Не доделал, срок здачи подходил к концу, прошу разобрать)Запутался