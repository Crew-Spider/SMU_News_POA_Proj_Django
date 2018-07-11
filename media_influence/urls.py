from django.urls import path, re_path

from .api import medias_sentiment_count, medias_influence_score

app_name = "medai_influence"

urlpatterns = [
    re_path(
        r'^medias_sentiment_count/(?P<uni_name>[\w\W-]+)/(?P<sentiment>[\d-]+)/$', 
        medias_sentiment_count.medias_sentiment_count
    ), 
    re_path(
        r'^medias_influence_score/(?P<uni_name>[\w\W-]+)/(?P<sentiment>[\w\W-]+)/$', 
        medias_influence_score.medias_influence_score
    ), 
]
