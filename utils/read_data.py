import json
# File: readline-example-1.py
#f = open("train_factoid_1.json")  # 返回一个文件对象
def read_train_data():
    try:
       f= open(r'C:\Users\Jianrong\PycharmProjects\wenda\utils\train_factoid_1.json', mode='r', encoding='UTF-8')
       report_lines = f.readlines()
       for line in report_lines:
           #print(line.rstrip())
         # _s = json.loads(line)
           query = json.loads(line)['query']
           answer = json.loads(line)['answer']
           passage_text = json.loads(line)['passages'][1]['passage_text']
    finally:
        if f:
            f.close()