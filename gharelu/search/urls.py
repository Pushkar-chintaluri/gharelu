from django.urls import path
from . import views

urlpatterns=[
        path('predict/<str:name>/', views.predict, name='predict'),
        path('',views.index,name='index')]

