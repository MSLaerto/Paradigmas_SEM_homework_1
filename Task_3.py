#Вычисление факториала числа. Напишите программу, которая находит факториал заданного числа N с использованием рекурсии или встроенных функций.
import math 
def declarative_factorial(n):
    return math.factorial(n)
n = int(input("Введите N: "))
print(f"Поученный факториал {n}: {declarative_factorial(n)}")