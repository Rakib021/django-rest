from django.urls import path
from .views import StudentView, UserView

urlpatterns = [
    path('api/',StudentView.as_view()),
    path('register/',UserView.as_view()),
]
