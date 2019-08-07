from django.urls import path
from .views import (
    ArticleListView,
    ArticleCreateView,
    ArticleDeleteView,
    ArticleUpdateView,
    ArticleDetailView
)
urlpatterns =[
    path('',ArticleListView.as_view()),
    path('<pk>',ArticleDetailView.as_view()),
    path('',ArticleCreateView.as_view()),
    path('<pk>/delete',ArticleDeleteView.as_view()),
    path('<pk>/update',ArticleUpdateView.as_view()),
    
]