from django.urls import path
from . import views
from .views import *



urlpatterns=[
    path('',HouseInfoView.as_view(),name='index'),
    path('Second-form',BulbFormView.as_view(),name='Second-form'),

]