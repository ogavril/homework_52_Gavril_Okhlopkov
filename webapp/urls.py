from django.urls import path
from webapp.views import index_view, list_add, delete_list, show_list

urlpatterns = [
    path('', index_view, name="index"),
    path('add/', list_add, name="add"),
    path('delete/<int:pk>/', delete_list, name="delete"),
    path('<int:pk>/', show_list, name="show"),
]
