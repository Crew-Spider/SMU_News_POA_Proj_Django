import sys, os
sys.path.append(
    os.path.dirname(os.path.dirname(
        os.path.abspath(__file__)
    ))
)
from db_operation.connection import get_connected_database
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest



def medias_influence_score(request, **kwargs):
    if not (kwargs.get("uni_name") and kwargs.get("sentiment")):
        return HttpResponseBadRequest()
    
    if kwargs["sentiment"] not in ["-1", "0", "1", "all"]:
        return HttpResponseBadRequest()

    content = _medias_influence_score(kwargs["sentiment"], kwargs["uni_name"])
    return JsonResponse(content)


def _medias_influence_score(sentiment="all", university_name="all"):
    data_filter = {}
    if university_name != "all":
        data_filter["Uname"] = university_name
    
    if sentiment != "all":
        data_filter["sentiment"] = sentiment

    db = get_connected_database()
    news_of_uni = db.get_collection('newslist').find(data_filter)
    medias_influence_score = {}
    for news in news_of_uni:
        if medias_influence_score.get(news["media"]) is not None:
            medias_influence_score[news["media"]] += 1/(float(news["ranking"])/10+1)
        else:
            medias_influence_score[news["media"]] = 1/(float(news["ranking"])/10+1)
    
    return medias_influence_score