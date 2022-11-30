# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def InputNumbers(inputText):
    oks = False
    while not oks:
        try:
            number = float(input(f"{inputText}"))
            oks = True
        except ValueError:
            print("Это не число!")
    return number

def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum


num = InputNumbers("Введите число: ")

print(f"Сумма цифр = {sumNums(num)}")