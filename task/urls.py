from django.urls import path
from task.views import HomeView, ResultView

urlpatterns = [
    path('', HomeView.as_view(template_name="home.html"), name="home"),
    path('result', ResultView.as_view(template_name="result.html"),  name="result"),
]
