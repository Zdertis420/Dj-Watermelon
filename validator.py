M = ["Весёлое", "Спокойное", "Грустное"]
O = ["Тренируюсь", "Отдыхаю", "В дороге", "Работаю-Учусь"]


def validateMood(mood):
    words = [_.lower() for _ in mood.split()]
    for word in words:
        if 'весёл' in word or 'весел' in word or 'энер' in word or 'позитив' in word or 'хорош' in word or\
                'огонь' in word or 'офиг' in word or 'лучше' in word:
            return M[0]
        if 'спок' in word or 'дзен' in word or 'норм' in word or 'обычн' in word:
            return M[1]
        if 'грус' in word or 'грущ' in word or 'депрес' in word or 'плох' in word or 'ужас' in word or\
                'так' in word or 'хуже' in word or 'худш' in word:
            return M[2]
    return 'Жопа!'


def validateOccupation(occupation):
    words = [_.lower() for _ in occupation.split()]
    for word in words:
        if 'трен' in word or 'бег' in word or 'кача' in word or 'спорт' in word:
            return O[0]
        if 'отдых' in word or 'чил' in word or 'сижу' in word or 'лежу' in word or 'ем' in word or 'хав' in word or\
                'куша' in word or 'игр':
            return O[1]
        if 'дорог' in word or 'пут' in word or 'еду' in word or 'едем' in word or 'двиг' in word or 'движ' in word:
            return O[2]
        if 'работ' in word or 'учу' in word or 'заним' in word or 'дел' in word or 'защи' in word or 'тест' in word or\
                'пиш' in word or 'программир' in word or 'програмир' in word:
            return O[3]
    return 'Жопа!'












