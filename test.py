sleep(1)
await mess.answer(text='Приветсвую!\n'
                       'Хочешь крутой музон? тогда ответь на парочку моих вопросов')
sleep(0.5)
await dj.send_message(text='1. Как настроение? Весело, грустно, или может ты словил дзен?\n'
                           '2. Чо делвешь?\n',
                      chat_id=mess.from_user.id)

global mood, occupation, genre
mood = await getMoodOrOccupation(mess)
occupation = await getMoodOrOccupation(mess)
await askGenre
genre = callbackGenre()