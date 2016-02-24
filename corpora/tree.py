#обработка статей

import re
import lxml.html
import os
import subprocess

os.mkdir('text') 
os.mkdir('mystem_xml')
os.mkdir('mystem_txt')
f = open('articles.csv', 'w', encoding = 'utf-8')
f.write('path;author;sex;birthday;header;created;sphere;genre_fi;type;topic;chronotop;style;audience_age;audience_level;audience_size;source;publication;publisher;publ_year;medium;country;region;language\n')
sources = [] #здесь будет хранится список обработанных статей на случай, если одна статья будет находиться на нескольких страницах, отличающихся только категорией новости

for root, dirs, files in os.walk("vperyod\\"): #извлекаем данные для таблицы
    for name in files:
        try:
            page = open(os.path.join(root, name), encoding = 'utf-8')
            page = page.read()
            tree = lxml.html.fromstring(page)
            try:
                author = tree.xpath('.//span[@class="b-object__detail__author__name"]/text()')[0]
            except:
                author = 'Noname'
            sex = ''
            birthday = ''
            header = tree.xpath('.//head//title/text()')[0]
            header = re.split('\s\-', header)[0]
            created = tree.xpath('.//div[@class="b-basic-info"]//div//div//div//span[@class="date"]/text()')[0]
            sphere = 'публицистика'
            genre_fi = ''
            Type = ''
            topics = tree.xpath('.//div[@class="b-category-list-inline-2"]//a/text()')
            topic = ''
            for word in topics:
                topic += word + ' '
            chronotop = ''
            style = 'нейтральный'
            audience_age = 'н-возраст'
            audience_level = 'н-уровень'
            audience_size = 'районная'
            source = tree.xpath('.//meta[@property="og:url"]')[0].get('content')
            source = re.split('\?', source)[0]
            if source in sources:
                continue
            else:
                sources.append(source)
            publication = 'Вперёд'
            publisher = ''
            date = re.split('\.', created)
            publ_year = date[2]
            medium = 'газета'
            country = 'Россия'
            region = 'Ульяновская область'
            language = 'ru'
            address = re.split('\.', name)[0]
            month = date[1]
            Path = 'text\\' + publ_year + '\\' + month + '\\' + address + '.txt' #путь до будущего текста
            f.write(Path + ';' + author + ';' + sex + ';' + birthday + ';' + header + ';' + created + ';' + sphere + ';' + genre_fi + ';' + Type + ';' + topic + ';' + chronotop + ';' + style + ';' + audience_age + ';' + audience_level + ';' + audience_size + ';' + source + ';' + publication + ';' + publisher + ';' + publ_year + ';' + medium + ';' + country + ';' + region + ';' + language + ';' +'\n')
            #создаём текстовый файл
            try:
                descr = tree.xpath('.//meta[@property="og:description"]')[0].get('content')
            except:
                descr = ''
            article = tree.xpath('.//body//div[@class="b-page-wrapper"]//div[@class="b-block-text"]//div//div//*/text()')
            #сохраняем текст по заданному пути
            if os.path.exists('text\\' + publ_year + '\\' + month) == False:
                if os.path.exists('text\\' + publ_year) == False:
                    os.mkdir('text\\' + publ_year)
                    os.mkdir('mystem_xml\\' + publ_year)
                    os.mkdir('mystem_txt\\' + publ_year)
                os.mkdir('text\\' + publ_year + '\\' + month)
                os.mkdir('mystem_xml\\' + publ_year + '\\' + month)
                os.mkdir('mystem_txt\\' + publ_year + '\\' + month)
            text = open(Path, 'w', encoding = 'utf-8')
            text.write(descr + '\n\n')
            for line in article:
                line = line.replace(u'\xa0', u'') #убираем неразрывый пробел аскии
                text.write(line + ' ')
            text.close()
            #обрабатываем текст майстем
            subprocess.call(['E:\\corpora\\mystem', '-cigd', 'E:\\corpora\\' + Path, 'E:\\corpora\\mystem_txt\\' + publ_year + '\\' + month + '\\' + address + '.txt'])
            subprocess.call(['E:\\corpora\\mystem', '-cigd', '--format', 'xml', 'E:\\corpora\\' + Path, 'E:\\corpora\\mystem_xml\\' + publ_year + '\\' + month + '\\' + address + '.xml'])
            #перезаписываем файл с шапкой вверху
            text = open(Path, 'r+', encoding = 'utf-8')
            textRead = text.read()
            text.seek(0)
            text.truncate()
            text.write('@au ' + author + '\n@ti ' + header + '\n@da ' + created + '\n@topic ' + topic + '\n@url ' + source + '\n\n' + str(textRead))
            text.close()
            print(Path)
        except:
            continue
f.close()
