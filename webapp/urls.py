from django.urls import path
from webapp.views.list_views import IndexView, ListCreateView, ListDeleteView, ListView, ListUpdateView
from webapp.views.project_views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView

urlpatterns = [
    # path('', IndexView.as_view(), name="index"),
    path('add/', ListCreateView.as_view(), name="add"),
    path('delete/<int:pk>/', ListDeleteView.as_view(), name="delete"),
    path('<int:pk>/', ListView.as_view(), name="show"),
    path('list/<int:pk>/update', ListUpdateView.as_view(), name="update"),
    path('', ProjectListView.as_view(), name="projects"),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name="project"),
    path('projects/create', ProjectCreateView.as_view(), name="create_project"),
    path('projects/<int:pk>/update', ProjectUpdateView.as_view(), name="project_update"),
]
