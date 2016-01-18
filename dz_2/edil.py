import re
dic = {}
f = open('edil_2.html', encoding = 'utf-8')
entry = f.read()
entry = re.split('<', entry)
for line in entry:
    match = re.search('headword_id', line)
    if match != None:
        lemma = re.split('>', line)
        lemma = lemma[1]
        print(lemma)
for line in entry:
    match = re.search('Forms', line)
    if match != None:
        forms = re.split('\t|\s*', line)
        forms = forms[2:]
        for form in forms:
            form = form.strip(',')
            print(form)
            dic[form] = lemma
print(dic)
