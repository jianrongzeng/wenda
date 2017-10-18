import json
# File: readline-example-1.py
#f = open("train_factoid_1.json")  # 返回一个文件对象
try:
   f= open('train_factoid_1.json', mode='r', encoding='UTF-8')
   report_lines = f.readlines()
   for line in report_lines:
       #print(line.rstrip())
     # _s = json.loads(line)
       print(json.loads(line)['query'])
       print(json.loads(line)['answer'])
       print(json.loads(line)['passages'][1]['passage_text'])
finally:
    if f:
        f.close()