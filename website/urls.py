from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home_index'),
    path('bidule', views.bidule, name='home_bidule'),
    path('messages', views.all_messages, name='all_messages'),
    path('messages/new', views.new_message, name='new_message'),
    path('messages/edit/<str:id>', views.edit_message, name='edit_message'),
    path('messages/delete/<str:id>', views.delete_message, name='delete_message'),
    path('messages/<str:id>', views.show_message, name='show_message')

]

