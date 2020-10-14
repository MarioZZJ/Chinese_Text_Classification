import sqlite3
import os
import json

fdir = r'../data/poet.tang'
# fdir = r'../data/poet.song'

sql = '''
    INSERT INTO poet.tang (id,title,author,paragraphs)
    VALUES (?,?,?,?)
'''

lists = sqlite3.connect(r'../data/database/poet_with_id.db')
c = lists.cursor()

countPoet = 0

for info in os.listdir(fdir):
    with open(fdir+'/'+info, mode='r', encoding='UTF-8') as file:
        content = file.read()
        list_json = json.loads(content)
        for item in list_json:
            id = item ['id']
            author = item['author']
            textlist = item['paragraphs']
            paragraphs = ''
            for line in textlist:
                paragraphs += line
                paragraphs += '\n'
            title = item['title']
            #print([id,title,author,paragraphs])
            try:
                c.execute(sql,[id,title,author,paragraphs])
            except sqlite3.IntegrityError:
                print(id+"作为id重复了！所在文件名是"+info)
        file.close()
        countPoet += 1
        print("\r已经插入"+str(countPoet)+"000/57000首诗.",end="")

lists.commit()
lists.close()