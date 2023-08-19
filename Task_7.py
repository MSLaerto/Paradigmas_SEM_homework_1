#Поиск подстроки. Напишите программу, которая находит все вхождения заданной подстроки в строке с использованием встроенных функций.
def get_positions(s, subs):
    res = []
    pos = -1
    while True:
        pos = s.find( subs, pos + 1 )
        if pos == -1:
            break
        res.append(pos)
    return res
str1 = input("Введите строку:")
str2 = input("Введите подстроку:")
print(f"Индексы начала найденной подстроки :", *get_positions(str1, str2) )