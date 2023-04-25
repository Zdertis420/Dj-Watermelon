import sqlite3
import random


def recomend(li, Uid):
    M = ["Весёлое", "Спокойное", "Грустное"]
    O = ["Тренируюсь", "Отдыхаю", "В дороге", "Работаю-Учусь"]
    G = ["Джаз", "Классическая Музыка", "Поп-музыка", "Рок-металл", "Хип-хоп", "Шансон"]

    m = li[Uid][0]
    o = li[Uid][1]
    g = li[Uid][2]

    DB = "music/Dj-Арбуз музыка.db"
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

    answer = "Тогда тебе стоит послушать это:\n\n"
    n = 0
    for i in songs:
        n += 1
        if i != songs[-1]:
            answer += str(n) + ". " + i + "\n"
        else:
            answer += str(n) + ". " + i

    return answer

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
