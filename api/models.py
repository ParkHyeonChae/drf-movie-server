"""api/models.py"""

from django.db import models
import requests
import json


class MovieList(models.Model):
    title = models.CharField(max_length=50, verbose_name="영화제목")
    year = models.PositiveIntegerField(verbose_name='개봉년도')
    rating = models.FloatField(verbose_name='영화평점')
    genre = models.CharField(max_length=128, verbose_name='영화장르')
    summary = models.TextField(verbose_name='영화개요')

    class Meta:
        db_table = '영화리스트'
        verbose_name = '영화리스트'
        verbose_name_plural = '영화리스트'


# SQLite3에 yts api의 영화리스트 500개 저장 (admin페이지당 100개 출력 총 5페이지)

# def input_movielist(page):
#     api_url = 'https://yts.mx/api/v2/list_movies.json?sort_by=download_count&limit=50&page={}'.format(page)

#     data = requests.get(api_url)
#     json_data = json.loads(data.text)

#     for data in json_data['data']['movies']:

#         MovieList.objects.create(
#             title=data['title'],
#             year=data['year'],
#             rating=data['rating'],
#             genre=data['genres'],
#             summary=data['summary']
#         )


# for page in range(1, 11):
#     input_movielist(page)