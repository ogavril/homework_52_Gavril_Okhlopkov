from django.urls import path
from webapp.views import index_view

urlpatterns = [
    path('', index_view),
]