import os
import pickle
import jieba
import json
import time

def get_news_category_config():

    dataset_path = os.path.join(os.path.abspath('.'),'dataset','news_category_dataset')


    return {
            "categories": ["activity", "entrance", "social","study"],
            "load_files_path": dataset_path,
            "save_model_path": os.getcwd() +'/models/news_category_model.m',
            "count_vect_path": os.getcwd() +'/models/news_category_count_vect.dat',
            "tfidf_path": os.getcwd() +'/models/news_category_tfidf.dat'
    }


def get_news_sentiment_config():
    dataset_path = os.path.join(os.path.abspath('.'), 'dataset', 'news_sentiment_dataset')

    return {
        "categories": ["-1","0","1"],
        "load_files_path": dataset_path,
        "save_model_path": os.getcwd() + '/models/news_sentiment_model.m',
        "count_vect_path": os.getcwd() + '/models/news_sentiment_count_vect.dat',
        "tfidf_path": os.getcwd() + '/models/news_sentiment_tfidf.dat'
    }



def load_json_file(news_path):
    with open(news_path,'r',encoding="utf-8") as json_file:
        news_json = json.load(json_file)
        return news_json


def read_file(path):

    f = open(path,"r",encoding="utf-8")
    content = f.read()
    f.close()
    return content


def read_bunch_obj(path):

    file_obj = open(path,"rb")

    bunch = pickle.load(file_obj,encoding="iso-8859-1")

    file_obj.close()
    return bunch


def write_bunch_obj(path,bunchobj):

    file_obj = open(path,"wb")
    pickle.dump(bunchobj,file_obj)
    file_obj.close()


def seg_chinese_text(text):

    str = text.strip().replace("\r\n","").strip()
    text_seg = " ".join(jieba.cut(str))

    return text_seg


def get_tfidf_model(text,count_vect_path,tfidf_path):

    seg_text = seg_chinese_text(text)

    docs = []
    docs.append(seg_text)

    count_vect = read_bunch_obj(count_vect_path)
    tfidf_transformer = read_bunch_obj(tfidf_path)

    X_new_counts = count_vect.transform(docs)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)

    return X_new_tfidf


# 定义一个计算程序运行耗时的类
class Timer:

    def __init__(self):
        self.__start = 0.0
        self.__end = 0.0

    def getStart(self):
        self.__start = time.time()
        return self

    def getEnd(self):
        self.__end = time.time()
        return self

    def printTime(self):
        print("耗时为:",self.__end - self.__start)