from django.urls import path, include
from articles import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name="index"),
    path('<int:article_id>/', views.ArticleDetail.as_view(), name="article_view"),
]
