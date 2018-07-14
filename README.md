# SMU_News_POA_Proj_Django

运行须知:

1. 使用本地django时,把template/js/config.js里的djangoIpAddress改成127.0.0.1,再使用python manage.py runserver

2. 本地mongo设置需与media_influence/config/database.py中的设置一致,如需访问服务器,服务器地址为188.166.65.59

3. 后端数据接口在media_influence/api

4. 排序和图表在template/js/influence_rank_chart.js和template/js/sentimente_rank_chart.js

5. media_influence/crawler/crawler_news.py第175行，清空数据库,请使用该语句以使得爬虫重新爬取新数据,并且删除旧数据
