from django.urls import path
from .views import RobotView, RobotUpdateDeleteView, download, report


urlpatterns = [
    path('reports/', report, name='report'),
    path('repors/download/', download, name='download'),
    path('robots/', RobotView.as_view()),
    path('robots/<int:robot_id>/', RobotUpdateDeleteView.as_view()),
]
