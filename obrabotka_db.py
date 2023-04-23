import sqlite3
import random


M = ["Весёлое", "Спокойное", "Грустное"]
O = ["Тренируюсь", "Отдыхаю", "В дороге", "Работаю-Учусь"]
G = ["Джаз", "Классическая Музыка", "Поп-музыка", "Рок-металл", "Хип-хоп", "Шансон"]

m = M[2]
o = O[1]
g = G[4]

DB = "watermelow.db"
connection = sqlite3.connect(DB)
cur = connection.cursor()

table = cur.execute(f"""SELECT id FROM main WHERE mood='{m}' AND occupation='{o}' AND genre='{g}'""").fetchall()
table = "t" + str(table[0][0])
result = cur.execute(f"""SELECT song FROM {table}""").fetchall()
random.shuffle(result)
n = 3
songs = result[n-3:n]
for i in range(len(songs)):
    songs[i] = songs[i][0]

answer = "Тогда тебе стоит послушать это:\n"
for i in songs:
    if i != songs[-1]:
        answer += i + "\n"
    else:
        answer += i

print(answer)

# n += 3
# if n == 21:
#     print("Нет")
# else:
#     songs = result[n-3:n]
#     for i in range(len(songs)):
#         songs[i] = songs[i][0]
#
#     answer = ""
#     for i in songs:
#         if i != songs[-1]:
#             answer += i + "\n"
#         else:
#             answer += i
