import re
import os
import lxml.html
import math

def dictionary(directory, dic):
    words = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            f = open(os.path.join(root, name), encoding = 'utf8').read()
            print(name)
            tree = lxml.html.fromstring(f)
            doc = tree.xpath('.//doc/text()')
            for line in doc:
                line = line.lower()
                line = re.split('\s', line)
                for word in line:
                    word = word.strip('[()«»“”„=\'",.†—%<>-—„”?!:;]')
                    word = re.sub('[\(\)«»“”„\[\]=\\\'\"\,\.†—%\<\>\-—„”\?\!\:\;]', '\n', word)
                    match = re.search('\d|=|\.', word)
                    if match == None and word != '–' and word != '':
                        if word not in words:
                            words.append(word)
    fDic = open(dic, 'w', encoding = 'utf8')
    for word in words:
        fDic.write(word +'\n')
    fDic.close()
    print('my dic')

def morphemes(dic, morph):
    fDic = open(dic, encoding = 'utf8').readlines()
    words = []
    morphs = []
    fMorph = open(morph, 'w', encoding = 'utf8')
    j = 0
    for line in fDic:
        matches = 200
        i = -2
        if line not in words:
            while matches >= 200 and (len(line) - 1) > -i:
                wordlist = matches
                matches = 0
                if line[i:-1] not in morphs:
                    for line1 in fDic:
                        if (len(line1) - 1) > -i:
                            match = re.match(re.escape(line[i:-1]), re.escape(line1[i:-1]))
                            if match != None:
                                matches += 1
                i = i - 1
            words.append(line)          
            if wordlist > 200:                
                if line[(i+2):-1] not in morphs:
                    morphs.append(line[(i+2):-1])
                    fMorph.write(line[(i+2):-1] + '\n')
                    j+= 1
                    print(j)
    fMorph.close()

def text(doc, morphemes, result):
    fText = open(doc, encoding = 'utf8').read()
    fText = re.split('\s', fText)
    fMorph = open(morphemes, encoding = 'utf8').readlines()
    morphDic = []
    for mr in fMorph:
        morphDic.append(mr[:-1])
    fTextP = open(result, 'w', encoding = 'utf8')
    for word in fText:
        word = word.lower()
        word = word.strip('[()«»“”„=\'",.†—%<>-—„”?!:;]')
        word = re.sub('[\(\)«»“”„\[\]=\\\'\"\,\.†—%\<\>\—„”\?\!\:\;]', '', word)
        i = -1
        root = word
        morph = ''
        while len(word) >= -i:
            if word[i:] in morphDic:
                morph = word[i:]
                root = word[:i]
                i = i - 1
            else:
                break
        fTextP.write(root + ' + ' + morph + '\n')
    fTextP.close()

#dictionary('C:\\Users\\Lyubov\\Documents\\kirgiz\\text\\AA', 'C:\\Users\\Lyubov\\Documents\\kirgiz\\my_dic.txt')
morphemes('C:\\Users\\Lyubov\\Documents\\kirgiz\\my_dic.txt', 'C:\\Users\\Lyubov\\Documents\\kirgiz\\morphs.txt')
text('C:\\Users\\Lyubov\\Documents\\kirgiz\\text.txt', 'C:\\Users\\Lyubov\\Documents\\kirgiz\\morphs.txt', 'C:\\Users\\Lyubov\\Documents\\kirgiz\\text_parsed.txt')
