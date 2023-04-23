M = ["весёлое", "спокойное", "грустное"]
O = ["тренировки", "отдыха", "дороги", "работы"]


def validateMood(mood):
    words = [_.lower() for _ in mood.text.split()]
    for word in words:
        if 'весёл' in word or 'весел' in word or 'энер' in word:
            return M[0]
        if 'спок' in word or 'дзен' in word:
            return M[1]
        if 'грус' in word or 'грущ' in word or 'депрес' in word:
            return M[2]
        return None


def validateOccupation(occupation):
    words = [_.lower() for _ in occupation.text.split()]
    for word in words:
        if 'трен' in word:
            return O[0]
        if 'отдых' in word or 'чил' in word:
            return O[1]
        if 'дорог' in word or 'пут' in word:
            return O[2]
        if 'работ' in word:
            return O[3]
        return None





