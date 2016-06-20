from lxml import etree
import lxml.html
import os
import math
import re

def one_file(directory, new):
    fNew = open(new, 'w', encoding = 'utf8')
    fNew.write('<?xml version="1.0" encoding="utf-8"?>\n<html>\n<head>\n</head>\n<body>')
    doc2 = ''
    idPara = 0
    for root, dirs, files in os.walk(directory):
        for name in files:
            ff = open(os.path.join(root, name), encoding = 'utf-8').read()
            treeP = lxml.html.fromstring(ff)
            paras = treeP.xpath('.//para')
            for para in paras:
                para.set('id', str(idPara))
                para = etree.tostring(para, encoding = 'unicode', pretty_print = True)
                fNew.write(para)
                idPara += 1
    fNew.write('</body>\n</html>')
    print('done')
    fNew.close()
    return(new)

def compare (original, another):
    f = open(original, encoding = 'utf8')
    tree = etree.parse(f)
    ens = tree.xpath('.//se[@lang="en"]/text()')
    fNew = open(another, encoding = 'utf8')
    treeN = etree.parse(fNew)
    uks = treeN.xpath('.//se[@lang="uk"]')
    for en in ens:
        for ukT in uks:
            uk = ukT.text
            if uk != None:
                if en == uk:
                    break
                else:
                    i = 1
                    common = 0
                    nm = 0
                    while i < len(en) - 2 and i < len(uk) - 2:
                        try:
                            match = re.search(en[i:i+3], uk)
                            if match != None:
                                common += 1
                                nm = nm - 1
                            else:
                                nm += 1
                            if nm > 3:
                                break
                            i +=1
                        except:
                            break
                    amount = (len(en) + len(uk)) / 2
                    diff = 1 - (common / amount)
                    if diff < 0.2:
                        uk = en
                        ukT.text = uk
    fNew.close()
    allText = etree.tostring(treeN, encoding = 'unicode', pretty_print = True)
    fNew = open(another, 'w', encoding = 'utf8')
    fNew.write(allText)
    fNew.close()

compare('\\Pnin\\pnin_barabtarlo.xml', one_file('\\Pnin\\Pnin_nosik', 'pnin_nosik__processed.xml'))
