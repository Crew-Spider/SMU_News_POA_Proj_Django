import sys, os
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)
)))
from text_classification.news_category_train import predict_news_category
from text_classification.news_sentiment_train import predict_news_sentiment
from db_operation.connection import get_connected_database
import threading



def predict_news_category_and_sentiment(string):

    sentiment_result = predict_news_sentiment(string)
    category_result = predict_news_category(string)

    return {
        "news_sentiment":sentiment_result,
        "news_category": category_result
    }

def save_prediction_to_db():
    db = get_connected_database()
    news_list = db.get_collection('newslist')
    all_news = news_list.find({})
    threads = []
    for news in all_news:
        result = predict_news_category_and_sentiment(news['body'])
        thread = threading.Thread(
            target=_save_one_prediction_to_db,
            args=(result, news, news_list)
        )
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        print("剩余:" + str(threading.active_count()))
        thread.join()
    
    print("全部结束")
        

def _save_one_prediction_to_db(result, news, news_list):
    news_list.update_one(
        {
            "_id": news["_id"]
        },
        {
            "$set": {
                "classification": result["news_category"],
                "sentiment": result["news_sentiment"],
            }
        }
    )
    print("A thread of " + str(news["_id"]) + " " + news["Uname"] + " is ended")

if __name__ == '__main__':

    save_prediction_to_db()