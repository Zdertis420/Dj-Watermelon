import sqlite3
import random


def recomend(li, Uid):
    m = li[Uid][0]
    o = li[Uid][1]
    g = li[Uid][2]

    DB = "watermelow.db"
    connection = sqlite3.connect(DB)
    cur = connection.cursor()

    table = cur.execute(f"""SELECT id FROM main WHERE mood='{m}' AND occupation='{o}' AND genre='{g}'""").fetchall()
    if table[0][0] < 10:
        table = "t" + "0" + str(table[0][0])
    else:
        table = "t" + str(table[0][0])
    result = cur.execute(f"""SELECT song FROM {table}""").fetchall()
    random.shuffle(result)

    n = 3
    songs = result[:n]
    for i in range(len(songs)):
        songs[i] = songs[i][0]

    answer = ""
    k = 0
    for i in songs:
        k += 1
        if i != songs[-1]:
            answer += str(k) + ". " + i + "\n"
        else:
            answer += str(k) + ". " + i

    return answer


def recomendRM():
    M = ["Весёлое", "Спокойное", "Грустное"]
    O = ["Тренируюсь", "Отдыхаю", "В дороге", "Работаю-Учусь"]
    G = ["Джаз", "Классическая Музыка", "Поп-музыка", "Рок-металл", "Хип-хоп", "Шансон"]

    m = random.choice(M)
    o = random.choice(O)
    g = random.choice(G)

    DB = "watermelow.db"
    connection = sqlite3.connect(DB)
    cur = connection.cursor()

    table = cur.execute(f"""SELECT id FROM main WHERE mood='{m}' AND occupation='{o}' AND genre='{g}'""").fetchall()
    if table[0][0] < 10:
        table = "t" + "0" + str(table[0][0])
    else:
        table = "t" + str(table[0][0])
    result = cur.execute(f"""SELECT song FROM {table}""").fetchall()

    songs = result[:5]
    answer = "Ну вот тебе несколько песен, просто кайфовое музло, йоу\n\n"
    k = 0
    for i in songs:
        k += 1
        if i != songs[-1]:
            answer += str(k) + ". " + i + "\n"
        else:
            answer += str(k) + ". " + i

    return answer


# def recomendMore(li, Uid):
#     n += 3
#     if n == 21:
#         print("Нет")
#     else:
#         songs = result[n - 3:n]
#         for i in range(len(songs)):
#             songs[i] = songs[i][0]
#
#         answer = ""
#         k = 0
#         for i in songs:
#             k += 1
#             if i != songs[-1]:
#                 answer += str(k) + ". " + i + "\n"
#             else:
#                 answer += str(k) + ". " + i
#
#     return answer
