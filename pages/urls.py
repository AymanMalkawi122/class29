from django.urls import path

from .views import HomePageView, AboutPageView

from tasks.views import TaskListView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("tasks/", TaskListView.as_view(), name="task_list")
]
