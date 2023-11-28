from django.urls import path
from webapp.views import index_view, list_add, delete_list

urlpatterns = [
    path('', index_view),
    path('add/', list_add),
    path('delete/', delete_list),
]