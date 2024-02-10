from django.urls import path
from .views import StudentView

urlpatterns = [
    path('api/',StudentView.as_view()),
]
