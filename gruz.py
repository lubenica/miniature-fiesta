import re
f = open('gruz.txt', encoding = 'utf8')
fRead = open('gruz_text.txt', encoding = 'utf8')
fNew = open('gruz_output.txt', 'w', encoding = 'utf8')
dic = {}
abc = f.read()
abc = re.split('\n', abc)
for line in abc:
    letters = re.split('\t', line)
    dic[letters[0]] = letters[2]
text = fRead.read()
for s in text:
    if s in dic:
        text = text.replace(s, dic[s])
fNew.write(text)
f.close()
fNew.close()
