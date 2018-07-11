import sys, os
sys.path.append(
    os.path.dirname(os.path.dirname(
        os.path.abspath(__file__)
    ))
)
from db_operation.connection import get_connected_database
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest



def medias_sentiment_count(request, **kwargs):
    if not (kwargs.get("uni_name") and kwargs.get("sentiment")):
        return HttpResponseBadRequest()
    
    if kwargs["sentiment"] not in ["-1", "0", "1"]:
        return HttpResponseBadRequest()

    content = _medias_sentiment_count(kwargs["sentiment"], kwargs["uni_name"])
    return JsonResponse(content)


def _medias_sentiment_count(sentiment="-1", university_name="all"):
    data_filter = {
        "sentiment": sentiment
    }
    if university_name != "all":
        data_filter["Uname"] = university_name

    db = get_connected_database()
    news_of_uni = db.get_collection('newslist').find(data_filter)
    medias_count = {}
    for news in news_of_uni:
        if medias_count.get(news["media"]) is not None:
            medias_count[news["media"]] += 1
        else:
            medias_count[news["media"]] = 1
    
    return medias_count


if __name__ == '__main__':
    _medias_sentiment_count()