#Упорядочивание списка. Напишите программу, которая сортирует список чисел в порядке возрастания с использованием пузырьковой сортировки или другого метода сортировки.
import random as rnd
def listgen():
    list = [rnd.randint(0, 999) for i in range(11)]
    print ("Исходный cписок:" , end = " ")
    for i in range(11):
        print(f"{list[i]}" , end = " ")
    return list
def bublesort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return(list)            
list = listgen()
print(f"\nОтсортированный список : {bublesort(list)}")                
