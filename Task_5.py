#Поиск простых чисел. Напишите программу, которая находит все простые числа в заданном диапазоне от 1 до N.
def primes(n):
    result = 0 
    for i in range(2 , n+1):
        flag = 1 
        for j in range(2 , i):
            if i%j == 0 :
                flag = 0
        if flag == 1 :
            print(f"{i}" , end = " ")
n = int(input("Введите N: "))
print(f"Простые числа от 1 до {n} : ")
primes(n)