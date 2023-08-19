#Поиск наименьшего числа в списке. Напишите программу, которая находит наименьшее число в заданном списке с помощью цикла.
import random as rnd
import array as arr

def listgen():
    list = [rnd.randint(0, 999) for i in range(11)]
    print ("Исходный cписок:" , end = " ")
    for i in range(11):
        print(f"{list[i]}" , end = " ")
    return list
def list_min(list):
    min_el = list[0]
    for i in range(len(list)):
        if list[i] < min_el:
            min_el = list[i]
    return min_el
list = listgen()        
print(f"\nМинимальный элемент в этом списке: {list_min(list)}")