from django.urls import path

from .views import RobotView, RobotUpdateDeleteView

urlpatterns = [
    path('robots/', RobotView.as_view()),
    path('robots/<int:robot_id>/', RobotUpdateDeleteView.as_view()),
]