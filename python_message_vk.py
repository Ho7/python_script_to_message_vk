# coding: utf-8

import vk
import time

# инфа для вкапи
vkapi = vk.API('id_app', ('login', 'pass'),)
a_token = '###'
session = vk.Session()
vkapi = vk.API(session, access_token = a_token)

# настройки времени
def get_time():
    time_now = time.ctime(time.time())
    time_now = time_now.split(' ')
    time_now = time_now[3][:2]
    time_now = int(time_now)
    return time_now

def get_last_message():
    ''' функция возвращает ид последнего сообщения '''
    messages_in = vkapi.messages.get(count=1)
    messages_out = vkapi.messages.get(out=1, count=1)
    message_in = messages_in[0]
    message_out = messages_out[0]

    if message_out > message_in:
        last_message = message_out+1
    else:
        last_message = message_in+1

    return last_message

def send_mesage(time_from, time_to, period, text, user_id, chat_id):
    ''' функция отправки сообщения
        time_from - от целое(час)
        time_to - до целое(час)
        period - периодичность целое(сек)
        text - сообщение строка
        user_id - кому целое
        chat_id - номер чата целое
    '''

    while time_to > get_time():
        while time_from == get_time():
            time.sleep(period)
            guide=get_last_message()
            vkapi.messages.send(user_id=user_id, chat_id=chat_id, message='Текст сообщения: '+text+' Время отправки: '+time.ctime(time.time())+' Отправлено с помощью скрипта "python_vk_message.py" by: DEV_HO7', guide=guide)
    return 0

send_mesage(time_from, time_to, period, text, user_id, chat_id)
