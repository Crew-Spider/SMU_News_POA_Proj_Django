from pymongo import MongoClient
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.grid_search import GridSearchCV
import numpy as np


# 用来测试的,并无他用


def test1():
    MONGO_HOST = "188.166.65.59"
    MONGO_PORT = 27017
    MONGO_DB = "NewsPOA"
    MONGO_USER = "userAdmin"
    MONGO_PASS = "Ad1310724518"
    connection = MongoClient(MONGO_HOST, MONGO_PORT)
    db = connection[MONGO_DB]
    print(db)
    db.authenticate(MONGO_USER, MONGO_PASS)
    db = db.get_collection("newslist").find({})
    print (list(db))

def test2():
    categories = ["alt.atheism", "soc.religion.christian",
              "comp.graphics", "sci.med"]
    twenty_train = fetch_20newsgroups(subset="train",
                categories=categories, shuffle=True, random_state=42)
    print(twenty_train.target_names)
    
    
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(twenty_train.data)
    # 打印特征相关信息
    print("训练数据共有{0}篇, 词汇计数为{1}个".format(X_train_counts.shape[0], X_train_counts.shape[1]))
    # 查看某个词语的计数
    count = count_vect.vocabulary_.get(u'algorithm')
    print("algorithm的出现次数为{0}".format(count))


    # 使用TF-IDF提取文本特征
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    # 查看特征结果
    print(X_train_tfidf.shape)


    clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
    print("分类器的相关信息：")
    print(clf)

    # 预测用的新字符串，你可以将其替换为任意英文句子
    docs_new = ["Nvidia is awesome!"]
    # 字符串处理
    X_new_counts = count_vect.transform(docs_new)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)

    # 进行预测
    predicted = clf.predict(X_new_tfidf)

    # 打印预测结果
    for doc, category in zip(docs_new, predicted):
        print("%r => %s" % (doc, twenty_train.target_names[category]))

    # 建立Pipeline
    # text_clf = Pipeline([("vect", CountVectorizer()),
    #                     ("tfidf", TfidfTransformer()),
    #                     ("clf", MultinomialNB()),
    # ])
    text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge',
                                            penalty='l2',
                                            alpha=1e-3,
                                            max_iter=5,
                                            random_state=42)),
                    ])
    # 训练分类器
    text_clf = text_clf.fit(twenty_train.data, twenty_train.target)
    # 打印分类器信息
    print(text_clf)


    twenty_test = fetch_20newsgroups(subset="test",
                categories=categories, shuffle=True, random_state=42)
    # 使用测试数据进行分类预测
    predicted = text_clf.predict(twenty_test.data)
    # 计算预测结果的准确率
    print("准确率为：")
    print(np.mean(predicted == twenty_test.target))

    print("打印分类性能指标：")
    print(metrics.classification_report(twenty_test.target, predicted,
        target_names=twenty_test.target_names))
    print("打印混淆矩阵：")
    print(metrics.confusion_matrix(twenty_test.target, predicted))

    # 设置参与搜索的参数
    parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
                'tfidf__use_idf': (True, False),
                'clf__alpha': (1e-2, 1e-3),
    }

    # 构建分类器
    gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)
    print(gs_clf)

    # 使用部分训练数据训练分类器
    gs_clf = gs_clf.fit(twenty_train.data[:400], twenty_train.target[:400])
    # 查看分类器对于新文本的预测结果，你可以自行改变下方的字符串来观察分类效果
    twenty_train.target_names[gs_clf.predict(['An apple a day keeps doctor away'])[0]]

    gs_clf = gs_clf.fit(twenty_train.data[:400], twenty_train.target[:400])
    print("最佳准确率：%r" % (gs_clf.best_score_))

    for param_name in sorted(parameters.keys()):
        print("%s: %r" % (param_name, gs_clf.best_params_[param_name]))

if __name__ == "__main__":
    test1()