from django.urls import path
from .views import expense, delete_item, home

urlpatterns = [
    path('expense/', expense, name='expense'),
    path('', home, name='home'),
    path('delete/<uuid:uuid>', delete_item, name='delete_item')
]
