#Поиск уникальных элементов в списке. Напишите программу, которая создает новый список, содержащий только уникальные элементы из исходного списка.
import random as rnd
def listgen(sizeof_list):
    list = [rnd.randint(0, 9) for i in range(sizeof_list+1)]
    print ("Исходный cписок :  [" , end = "")
    for i in range(sizeof_list):
        print(f"{list[i]}" , end = ", ")
    print(f"{list[sizeof_list]}]")    
    return list
def declarative_list_cleaner(list):
    seen = set()
    return [x for x in list if not (x in seen or seen.add(x))]
sizeof_list = 20
list = listgen(sizeof_list)
print(f"Поученный список : {declarative_list_cleaner(list)}")