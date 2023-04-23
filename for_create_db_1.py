list_of_songs = '''   '''
list_of_songs = list_of_songs.split(", ")
for i in range(len(list_of_songs)):
    list_of_songs[i] = list_of_songs[i].replace('"', "'")

for i in list_of_songs:
    if i == list_of_songs[-1]:
        print(f'("{i[:-1]}")')
    else:
        print(f'("{i}"', end="), ")