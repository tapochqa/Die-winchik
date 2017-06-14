# -*- coding: utf-8 -*-
import vk_api
from time import sleep
from datetime import datetime
vinchik = -91050183

authlist = {'login': [], 'password': []}
vk_session = []

with open('logs', 'w') as log:
    log.write('')

#мультилогин
with open('logins', 'r') as logins:
    for line in logins:
        lnp = line.split(':')
        
        lnp[1] = lnp[1].replace(' \n', '') #убираем \n в конце строки
        
        authlist['login'].append(lnp[0])
        authlist['password'].append(lnp[1])

print authlist
for a in range (0, len(authlist['login'])):
    vk_session.append(vk_api.VkApi(authlist['login'][a], authlist['password'][a]))
    vk_session[a].auth()

def response (amessage, rmessage, resp, log):
    if amessage['items'][0]['body'].find(rmessage) != -1:
        vk.messages.send(user_id = vinchik, message = resp)
        d = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        with open('logs', 'a') as loga:
            loga.write (log + ' ' + d + '\n')
        sleep(3)

def core (vk):
    message = vk.messages.getHistory(count = 1, user_id = vinchik)
       
    response(message, u'Нашел кое-кого для тебя, смотри:', '1', 'ans 1')
    response(message, u'1. Оценить еще кого-то.', '1', 'ans 2')
    response(message, u'Кое-кому понравилось твое предложение', '1', 'ans 3')
    response(message, u'Есть новости по твоей анкете', '1', 'ans 4')
    response(message, u'Ждем ответа от этого пользователя', '1', 'ans 5')
    response(message, u'Кто-то тобой заинтересовался!', '1', 'ans 6')
    response(message, u'Отлично, нашли тебе компанию', '1', 'ans 7')

w = ''
with open ('work', 'r') as work:
    w = work.read()

while (w == '1'):
    for api in vk_session:
        with open ('work', 'r') as work:
            w = work.read()
        vk = api.get_api()
        core(vk)

    
