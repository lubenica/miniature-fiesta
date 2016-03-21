#-*- coding: utf-8 -*-

import re
import os
import codecs

def wiki_extractor(path):
    WikiE = path + '\WikiExtractor.py' + ' -o ' + path + ' ' + path + '\ltgwiki-20160305-pages-articles.xml'
    return WikiE

def no_tags(wiki):
    f = codecs.open(wiki, 'r', encoding = 'utf8')
    fNew = codecs.open('clear_wiki.txt', 'w', encoding = 'utf8')
    text = f.read()
    text = re.split('\n', text)
    for line in text:
        match = re.search('^<.*>',line)
        if match == None:
            fNew.write(line)
    f.close()
    fNew.close()
    return(fNew)

def frequencies(clearText):
    f = codecs.open(clearText, 'r', encoding = 'utf8')
    fFreq = codecs.open('freq_list.tsv', 'w', encoding = 'utf8')
    text = f.read()
    text = text.lower()
    text = re.split('\s|\"|\(|\/', text)
    dic = {}
    for line in text:
        word = line.strip(u'[\(\)\«\»\“\”\„\[\]\=\'\"\,\.\†\—\%\<\>\-\—\„\”\?\!\:\;\/\\]+')
        match = re.search('[\d\=\.]+', word)
        if match == None and word != u'–' and word != '':
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
    freqs = list(dic.items())
    freqs.sort(key = lambda item: item[1], reverse = True)
    for item in freqs:
        wrd = item[0]
        fFreq.write(wrd + '\t' + str(dic[wrd]) + '\n')
    f.close()
    fFreq.close()
        
os.system(wiki_extractor(os.getcwd()))
no_tags('AA\\wiki_00')
frequencies('clear_wiki.txt')
