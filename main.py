# -*- coding: utf-8 -*-
import vk_api
from time import sleep

vinchik = -91050183

authlist = {'login': [], 'password': []}
vk_session = []

#мультилогин
with open('logins', 'r') as logins:
    for line in logins:
        lnp = line.split(':')
        
        lnp[1] = lnp[1].replace(' \n', '') #убираем \n в конце строки
        
        authlist['login'].append(lnp[0])
        authlist['password'].append(lnp[1])
        
for a in range (0, len(authlist['login'])):
    vk_session.append(vk_api.VkApi(authlist['login'][a], authlist['password'][a]))
    vk_session[a].auth()

    def core (vk):
        message = vk.messages.getHistory(count = 1, user_id = vinchik)
        
        if message['items'][0]['body'].find(u'Нашел кое-кого для тебя, смотри:') != -1:
            vk.messages.send(user_id = vinchik, message = '1')
            print ('gotcha working')
            sleep(2)
            
        if message['items'][0]['body'].find(u'1. Оценить еще кого-то.') != -1:
            vk.messages.send(user_id = vinchik, message = '1')
            print ('gotcha pair')
            sleep(2)
            
        if message['items'][0]['body'].find(u'Кое-кому понравилось твое предложение') != -1:
            vk.messages.send(user_id = vinchik, message = '1')
            print ('gotcha response')
            sleep(2)
        if message['items'][0]['body'].find(u'Есть новости по твоей анкете') != -1:
            vk.messages.send(user_id = vinchik, message = '1')
            print ('gotcha smth')
            sleep(2)
            
        if message['items'][0]['body'].find(u'Ждем ответа от этого пользователя') != -1:
            vk.messages.send(user_id = vinchik, message = '1')
            print ('gotcha smth2')
            sleep(2)
        
while (228==228):
    for api in vk_session:
        vk = api.get_api()
        core(vk)
        
    
    
