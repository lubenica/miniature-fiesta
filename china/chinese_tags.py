import lxml.html
import re

def dic_new(dictionary):
    dctnr = open(dictionary, encoding = 'utf-8')
    dic = {}
    dctnr = dctnr.read()
    dctnr = dctnr.split('\n')
    for line in dctnr:
        line0 = line.split(' ')
        line1 = re.split('\[|\]', line)
        if len(line1) > 2:
            transcr = line1[1]
            meanings = []
            line2 = line.split('/')
            meanings = line2[1:-1]
            for indx, elem in enumerate(meanings):
                meanings[indx] = elem.replace(' ', '_')
            sem = ''
            for meaning in meanings:
                sem += meaning + ', '
            sem = sem[:-2]
            info = '<ana lex="'+ line0[1] + '" transcr="' + transcr + '" sem="' + sem + '"/>'
            if line0[1] in dic:
                dic[line0[1]] += info
            else:
                dic[line0[1]] = info
    return(dic)

def process(text, processed, dic):
    f = open(text, encoding = 'utf-8')
    fNew = open(processed, 'w', encoding = 'utf-8')
    fNew.write('<?xml version="1.0" encoding="utf-8"?>\n<html>\n<head>\n</head>\n<body>\n')
    f = f.read()
    tree = lxml.html.fromstring(f)
    for rus in tree.xpath('.//se[@lang="ru"]'):
        rus.getparent().remove(rus)
    ses = tree.xpath('.//se/text()')
    state = 'exists'
    for se in ses:
        i = -1    
        word = ''
        words = ''
        while i < len(se) - 1:
            if state == 'exists':
                i += 1
                word += se[i]
                if word not in dic:
                    state = 'not exists' 
            elif state == 'not exists':
                word = word[:-1]
                if word != '':
                    words += '<w>' + dic[word] + word + '</w>' + '\n'
                    word = ''
                    i += -1
                state = 'exists'
        if words != '':
            fNew.write('<se>\n' + words + '</se>\n')
    fNew.write('</body>\n</html>')
    fNew.close()

process('stal.xml', 'stal_processed.xml', dic_new('cedict_ts.u8'))
