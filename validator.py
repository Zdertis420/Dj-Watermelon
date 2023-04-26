M = ["Весёлое", "Спокойное", "Грустное"]
O = ["Тренируюсь", "Отдыхаю", "В дороге", "Работаю-Учусь"]


def validateMood(mood):
    word = mood.lower()
    if 'не' in word and ('весёл' in word or 'весел' in word or 'энер' in word or 'позитив' in word or 'хорош' in word or
                         'огонь' in word or 'офиг' in word or 'лучше' in word or 'боевое' in word or
                         'празднично' in word or 'замечательно' in word or 'превосходно' in word or 'добро' in word or
                         'великолепно' in word or 'лучезарн' in word or 'мечтатель' in word or 'радостно' in word or
                         'новогодн' in word or 'рождестенско' in word or 'супер' in word or 'огонь' in word or
                         'огнен' in word or 'класс' in word or 'победно' in word or 'чудесн' in word):
        return M[2]

    if 'весёл' in word or 'весел' in word or 'энер' in word or 'позитив' in word or 'хорош' in word or\
            'огонь' in word or 'офиг' in word or 'лучше' in word or 'боевое' in word or 'празднично' in word or\
            'замечательно' in word or 'превосходно' in word or 'добро' in word or 'великолепно' in word or\
            'лучезарн' in word or 'мечтатель' in word or 'радостно' in word or 'новогодн' in word or\
            'рождестенско' in word or 'супер' in word or 'огонь' in word or 'огнен' in word or 'класс' in word or\
            'победно' in word or 'чудесн' in word:
        return M[0]

    if 'спок' in word or 'дзен' in word or 'норм' in word or 'ничего' in word or 'прост' in word or\
            'обычн' in word or 'беззаботно' in word or 'мирно' in word or 'умиротвор' in word or\
            'сносно' in word:
        return M[1]

    if 'не' in word and ('грус' in word or 'грущ' in word or 'депрес' in word or 'плох' in word or 'ужас' in word or
                         'так' in word or 'хуже' in word or 'худш' in word or 'угрюм' in word or 'дурно' in word or
                         'вражд' in word or 'кисло' in word or 'раздраж' in word or 'гнетущ' in word or
                         'хмуро' in word or 'тревожно' in word or 'печаль' in word or 'уныл' in word or
                         'мерз' in word or 'смутн' in word or 'отврат' in word or 'тоск' in word):
        return M[0]

    if 'грус' in word or 'грущ' in word or 'депрес' in word or 'плох' in word or 'ужас' in word or\
            'так' in word or 'хуже' in word or 'худш' in word or 'угрюм' in word or 'дурно' in word or\
            'вражд' in word or 'кисло' in word or 'раздраж' in word or 'гнетущ' in word or 'хмуро' in word or\
            'тревожно' in word or 'печаль' in word or 'уныл' in word or 'мерз' in word or 'смутн' in word or\
            'отврат' in word or 'тоск' in word:
        return M[2]

    if len(word) <= 3:
        return M[0]
    elif len(word) <= 7:
        return M[1]
    else:
        return M[2]


def validateOccupation(occupation):
    word = occupation.lower()
    if 'трен' in word or 'бег' in word or 'кача' in word or 'спорт' in word or 'отжим' in word or 'присед' in word or\
            'подтяг' in word:
        return O[0]

    if 'отдых' in word or 'чил' in word or 'сижу' in word or 'лежу' in word or 'ем' in word or 'хав' in word or\
            'куша' in word or 'игр' in word:
        return O[1]

    if 'дорог' in word or 'пут' in word or 'еду' in word or 'едем' in word or 'двиг' in word or 'движ' in word or\
            'катаю' in word:
        return O[2]

    if 'работ' in word or 'учу' in word or 'заним' in word or 'дел' in word or 'защи' in word or 'тест' in word or\
            'пиш' in word or 'программир' in word or 'програмир' in word or 'код' in word or 'чит' in word:
        return O[3]

    return O[1]
