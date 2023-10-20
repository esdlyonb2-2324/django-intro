from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home_index'),
    path('bidule', views.bidule, name='home_bidule'),
    path('messages', views.all_messages, name='all_messages')

]

