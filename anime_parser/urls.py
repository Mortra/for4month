from django.urls import path
from . import views,models


app_name = 'scrapy_url'
urlpatterns = [
    path('', views.ParserFormView.as_view(), name="parser_view"),
    path('anime/', views.AnimeViews.as_view(), name='anime')
    ]