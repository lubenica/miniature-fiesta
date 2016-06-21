import random

def alllines(table):
    f = open(table, encoding = 'utf-8')
    f = f.readlines()
    lines = {}
    i = 0
    allwords = 0
    for line in f[1:]:
        line = line[:-2].split(';')
        if line[22] != 'none':
            if int(line[22]) > 80000:
                if int(line[22]) > 100000:
                    line.append('0.33')
                    line[22] = str(int(line[22]) // 3)
                    lines[i] = line
                    lines[i+1] = line
                    if int(line[22]) % 3 != 0:
                        line[22] += str(int(line[22]) // 3 + int(line[22]) % 3)
                    lines[i+2] = line
                    i += 3
                else:
                    line[22] = str(int(line[22]) // 2)
                    line.append('0.5')
                    lines[i] = line
                    if int(line[22]) % 2 != 0:
                        line[22] = str(int(line[22]) // 2 + int(line[22]) % 2)
                    lines[i+1] = line
                    i += 2
            else:
                line.append('1') 
                lines[i] = line
                i += 1
    random.shuffle(lines)
    return(lines)

def wordcount(table, lines, new):
    f = open(table, encoding = 'utf-8')
    f = f.readlines()
    fNew = open(new, 'w', encoding = 'utf-8')
    fNew.write(f[0][:-1] + 'part;\n')
    
    wordsH = 40000000
    wordsP = 29000000
    wordsM = 11464121
    wordsBE = 3698789
    wordsUN = 12000000
    wordsOD = 1563824
    wordsCB = 1596640
    wordsPT = 921346
    wordsR = 572650

    for i in lines:
        line = lines[i]
        sphere = line[6].split(' | ')
        sph1 = sphere[0]
        if sph1 == 'публицистика' and line[8] == 'мемуары':
            words = wordsM
        elif sph1 == 'публицистика' and line[8] != 'мемуары':
            words = wordsP
        elif sph1 == 'бытовая' or 'электронная коммуникация':
            words = wordsBE
        elif sph1 == 'художественная':
            words = wordsH
        elif sph1 == 'учебно-научная':
            words = wordsUN
        elif sph1 == 'официально-деловая':
            words = wordsOD
        elif sph1 == 'церковно-богословская':
            words = wordsCB
        elif sph1 == 'производственно-техническая':
            words = wordsPT
        elif sph1 == 'реклама':
            words = wordsR
        if words > 0:
            words += -int(line[22])
            for cell in line:
                fNew.write(cell + ';')
            fNew.write('\n')

    fNew.close()

wordcount('source_post1950_wordcount.csv', alllines('source_post1950_wordcount.csv'), 'source_post1950_result.csv')
