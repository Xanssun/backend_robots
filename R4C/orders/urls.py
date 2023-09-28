from django.urls import path

from .views import download, index

app_name = "orders"

urlpatterns = [
    path('', index, name='index'),
    path('download/', download, name='download'),
]