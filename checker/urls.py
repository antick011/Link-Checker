from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.check_link, name='check_link'),
]
