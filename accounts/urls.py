from django.urls import path
from .views import login_page, register, logout_page

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_page, name='logout')
]