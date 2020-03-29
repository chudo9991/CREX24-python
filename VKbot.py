import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


# API-ключ созданный ранее
token = "0b9aee0a485b1baa175d043043bb9a8657f7e2b6b2b93f4d18f080f00e791018f07861ec71f5a061e2465"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)
# Работа с сообщениями
longpoll = VkLongPoll(vk)
print("Бот запущен")

# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        # Сообщение от пользователя
            request = event.text
        # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "И вам не хворать!")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            elif request == "погода":
                write_msg(event.user_id, "https://yandex.ru/pogoda/petrozavodsk")
            elif request == "биткоин":
                write_msg(event.user_id, "https://www.google.com/search?safe=strict&rlz=1C1OKWM_ruRU815RU815&sxsrf=ALeKk00JgIOukN57tzQK_C2oEE6IXr0L5g%3A1582351702089&ei=VsVQXoOGBcX3qwH1-7-ICA&q=%D1%86%D0%B5%D0%BD%D0%B0+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0&oq=%D1%86%D0%B5%D0%BD%D0%B0+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0&gs_l=psy-ab.3..35i39i70i258j0l9.1956.7821..8604...4.1..0.136.2051.0j17......0....1..gws-wiz.......0i71j35i39j0i131j0i67j0i131i67j35i305i39i70i258j0i10j35i304i39i70i258j0i13.k5vpknwRruk&ved=0ahUKEwiDifO4v-TnAhXF-yoKHfX9D4EQ4dUDCAs&uact=5")
            else:
                write_msg(event.user_id, "Такому меня не учили!")