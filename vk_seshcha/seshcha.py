import vk
import re
import time

def auth(token):
    session = vk.Session(access_token = token)
    api = vk.API(session)
    return api

def corpus(api):
    seshcha = api.users.search(city = 5710, count = 1000, fields = 'sex, bdate, personal')
    f = open('seshcha.csv', 'w', encoding = 'utf8')
    f.write('first_name' + ';' + 'last_name' + ';' + 'uid'+ ';' + 'sex' + ';' + 'bdate'+ ';' + 'langs'+ ';' + 'posts' + '\n')
    seshcha = seshcha[1:]
    for line in seshcha:
        dic = dict(line)
        time.sleep(0.30)
        posts = api.wall.get(owner_id = dic['uid'], count = 2000)
        posts = posts[1:]
        wall = ''
        for line in posts:
            line = dict(line)
            if line['post_type'] == 'post' and 'text' in line:
                if line['from_id'] == dic['uid']:
                    if len(line['text']) > 1:
                        wall += line['text'] + '\n\n'
            elif 'copy_text' in line:
                if len(line['copy_text']) > 1:
                    wall += line['copy_text'] + '\n\n'
        if wall != '':
            txtName = 'seshcha_corpus\\' + str(dic['uid']) + '.txt'
            fTxt = open(txtName, 'w', encoding = 'utf8')
            fTxt.write(wall)
            fTxt.close()
            try:
                pers = dict(dic['personal'])
                if 'langs' in pers:
                    langs = pers['langs']
                    lang = ''
                    for l in langs:
                        lang += l + ', '
                    lang = lang[:-2]
            except KeyError:
                lang = ''
            try:
                bd = str(dic['bdate'])
            except KeyError:
                bd = ''
            f.write(dic['first_name'] + ';' + dic['last_name'] + ';' + str(dic['uid']) + ';' + str(dic['sex']) + ';' + bd + ';' + lang + ';' + txtName + '\n')
    f.close()

corpus(auth('df5faada646be9a54513d536d328c5bf462a4c06c3e77f4c98d3ac1cbfb0af9372b8c0301680384eadf18'))
