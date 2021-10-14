from django.urls import path

from .views import index, Receiver

urlpatterns = [
    path('', index, name='index'),
    path('upload', Receiver.as_view()),
]