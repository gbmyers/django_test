from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(r'<int:pk>/', views.DetailView.as_view(), name='detail'),
    path(r'<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path(r'<int:question_id>/vote/', views.vote, name='vote'),
]
