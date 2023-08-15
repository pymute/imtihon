from django.urls import path
from .views import (AllCreateView,DetailApiView,AllAvtorView,UpdateApiView,DeleteApiView)
from django.urls import path


urlpatterns = [
    path('get_all/',AllAvtorView.as_view()),
    path('get_by_avtorid/<int:pk>',DetailApiView.as_view()),
    path('create/',AllCreateView.as_view()),
    path('update/',UpdateApiView.as_view()),
    path('delete/<int:pk>/',DeleteApiView.as_view())
 ]


