#создаём папку со всеми страницами сайта

import urllib.request
import re

u = urllib.request.urlopen('http://inza-vpered.ru/')
f = u.read()
fNew = open('vperyod\\0.html', 'wb')
fNew.write(f)
fNew.close()

pages = [''] #список страниц
j = 0
i = 1
forbidden = ['news/send/', 'ad/create/'] #список страниц не подлежащих обработке

for page in pages:
    try:
        fRead = open('vperyod\\' + str(j) + '.html', encoding = 'utf-8') #достаём ссылки
        f = fRead.read()
        f = re.split('\n', f)
        for line in f:
            match = re.search('href="/', line)
            if match != None:
                line = re.split('<', line)
                for tag in line:
                    match = re.search('href="/', tag)
                    if match != None:
                        address = re.split('href="/', tag)
                        address = re.split('"', address[1])
                        address = address[0]
                        if address in pages or address in forbidden:
                            continue
                        else:
                            pages.append(address)
                            url = urllib.request.urlopen('http://inza-vpered.ru/' + address) #сохраняем страницу
                            file = url.read()
                            fileNew = open('vperyod\\' + str(i) + '.html', 'wb')
                            fileNew.write(file)
                            fileNew.close()
                            i += 1
    except:
        continue
    j += 1
