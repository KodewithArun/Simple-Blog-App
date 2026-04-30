from django.urls import path
from .views import home, create_post , post_details ,delete_post , edit_post , signup , login_view , logout_view

urlpatterns = [
    path("signup/",signup, name="signup"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('',home,name='home'),
    path('create/',create_post,name='create'),
    path('post/<int:id>/',post_details,name='detail'),
    path('delete/<int:id>/', delete_post, name='delete'),
    path('edit/<int:id>/', edit_post, name='edit'),
]