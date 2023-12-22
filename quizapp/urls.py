from django.urls import path, include

from .views import question, quiz, ResultList

urlpatterns = [
    path('', quiz, name='quiz'),
    path('quiz/<int:pk>/', question, name='quistion'),
    path('results/', ResultList.as_view(), name='results'),

]
