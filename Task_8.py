#Вычисление суммы цифр числа. Напишите программу, которая вычисляет сумму всех цифр заданного числа, используя математические операции и деление нацело.
def sum_of_numbers(n):
    return sum(map(int, str(n)))
n = int(input("Введите N: "))
print(f"Полученная сумма цифр числа {n} =" , sum_of_numbers(n))  