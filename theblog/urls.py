from .views import HomeView, ArticleDetailView
from django.urls import path
#from . import views

urlpatterns = [
    #path('',views.home, name="home")
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    #pk-->primary key 
    #, when creating entry they get assigned idnum assign primary key
]