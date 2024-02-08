

from django.urls import path 
from .views import *

urlpatterns = [
  path('api/',home),
  path("post/",data_post),
  path('update/<int:id>',data_update),
  path('delete/<int:id>',data_delete),
  path('book/',book_detail),


]
