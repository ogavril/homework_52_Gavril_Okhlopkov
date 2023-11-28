from django.urls import path
from webapp.views import index_view, list_add

urlpatterns = [
    path('', index_view),
    path('add/', list_add)
]