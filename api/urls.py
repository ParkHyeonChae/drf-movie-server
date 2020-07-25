"""api/urls.py"""

from django.urls import path
from . import views
from .yasg import *

app_name = 'api'


urlpatterns = [
    path('', views.MovieListViewSet.as_view()),
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]