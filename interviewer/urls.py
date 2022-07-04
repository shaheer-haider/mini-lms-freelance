from django.urls import path
from .views import interview, startInterview
urlpatterns = [
    path('start/', interview, name='interview' ),
    path('inter/',startInterview, name='inter' )
]


