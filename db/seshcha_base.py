import pymysql

connection = pymysql.connect(host = 'localhost', user = 'guest1', password = 'n76Je4=wx6H', db = 'guest1_ivanova', charset='utf8mb4')
cur = connection.cursor()
cur.execute('CREATE TABLE `people` (`person_id` INT(15), `name` VARCHAR(255), `surname` varchar(255), `sex` INT(1), `bdate` DATE, `posts` VARCHAR(255)) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci')
cur.execute('CREATE TABLE `langs` (`lang_id` INT(5), `lang` VARCHAR(255)) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci')
cur.execute('CREATE TABLE `pl` (`connection_id` INT(10), `person_id` INT(15), `lang_id` INT(5)) DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci')00
sql1 = 'INSERT INTO `people` (`person_id`, `name`, `surname`, `sex`, `bdate`, `posts`) VALUES (%c, %s, %s, %c, %c, %s)'
sql2 = 'INSERT INTO `langs` (`lang_id`, `lang`) VALUES (%c, %s)'
sql3 = 'INSERT INTO `pl` (`connection_id`, `person_id`, `lang_id`) VALUES (%c, %c, %c)'
f = open('seshcha.csv', encoding = 'utf8')
for line in f[1:]:
    info = line.split(';')
    nm = line[0]
    srnm = line[1]
    pId = line[2]
    sx = line[3]
    bdt = line[4]
    lngs = line[5]
    psts = line[6]
    lId = 0
    cId = 0
    lngs = lngs.split()
    cur.execute(sql1, (pId, nm, srnm, sx, bdt, psts))
    for lng in lngs:
        lng = re.strip(',', lng)
        if lng not in lngBase:
            cur.execute(sql2, (lId, lng))
            lId += 1
        cur.execute(sql3, (cId, pId, lId))
        cId += 1
connection.commit()
cur.close()
connection.close()
