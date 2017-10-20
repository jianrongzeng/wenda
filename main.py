import json
import jieba
import codecs
import jieba.posseg as pseg

if __name__ == '__main__':

    # def read_train_data():
        global lis_of_passages_aftercut
        lis_of_passages_aftercut = []
        global list_of_traindata_after_cut
        list_of_traindata_after_cut = []
        stopwords = [line.strip() for line in open(r'stopword.txt', 'r').readlines()]
        try:
            f = open(r'C:\Users\Jianrong\PycharmProjects\wenda\utils\train_factoid_1.json', mode='r', encoding='UTF-8')
            report_lines = f.readlines()
            # 取每一行，即一个“query”和“passages”
            with codecs.open('train_query_cut.txt', 'w+', 'utf-8') as f1:
                for line in report_lines:
                    # 对query进行分词
                    query_aftercut = " ".join(jieba.cut(json.loads(line)['query']))
                    data = ''
                    for word in query_aftercut:
                        if word not  in stopwords:
                            if word !='\t':
                                data +=word
                    f1.write(data.strip() + '\n')
            with codecs.open('train_passages_cut.txt', 'w+', 'utf-8') as f2:
                for line in report_lines:
                    list_of_passages = json.loads(line)['passages']
                    list_of_passage_text = [passage['passage_text']for passage in list_of_passages]
                    # print(list_of_passage_text)
                    passages_aftercut = " ".join(jieba.cut(" ".join(list_of_passage_text)))
                    data = ''
                    for word in passages_aftercut:
                        if word not in stopwords:
                            if word !='\t':
                                data +=word
                    f2.write(data.strip() + '\n')
            print("finished!")
        finally:
            if f:
                f.close()