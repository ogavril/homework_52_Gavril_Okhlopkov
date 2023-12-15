from django.urls import path
from webapp.views import IndexView, ListCreateView, ListDeleteView, ListView, ListUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('add/', ListCreateView.as_view(), name="add"),
    path('delete/<int:pk>/', ListDeleteView.as_view(), name="delete"),
    path('<int:pk>/', ListView.as_view(), name="show"),
    path('list/<int:pk>/update', ListUpdateView.as_view(), name="update"),
]
