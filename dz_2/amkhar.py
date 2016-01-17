f = open('amkhar.csv', encoding = 'utf8')
abc = f.read()
abc = abc.split('\n')
dic = {}
voc = abc[0].split('\t')
cons = []
i = 1
j = 0
del abc[0]
for line in abc:
    letter = line.split('\t')
    cons += letter[0]
    del letter[0]
    while i < len(voc):
        for con in letter:
            dic[con] = cons[j] + voc[i]
            i += 1
    i = 1
    j +=1
f.close()

fRead = open('amkhar_text.txt', encoding = 'utf8')
fNew = open('amkhar_output.txt', 'w', encoding = 'utf8')
text = fRead.read()
for s in text:
    if s in dic:
        text = text.replace(s, dic[s])
fNew.write(text)
fRead.close()
fNew.close()
