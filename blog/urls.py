from django.urls import path
from .views import home, create_post , post_details ,delete_post , edit_post

urlpatterns = [
    path('',home,name='home'),
    path('create/',create_post,name='create'),
    path('post/<int:id>/',post_details,name='detail'),
    path('delete/<int:id>/', delete_post, name='delete'),
    path('edit/<int:id>/', edit_post, name='edit'),
]