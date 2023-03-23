"""Path for URLs"""
from django.urls import path

from . import views

# Note this is used to determine the application namespace
# Used by django to determine how to identify this app
app_name = "polls"

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
