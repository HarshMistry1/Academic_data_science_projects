from unicodedata import name
from django.urls import path
from .views import home,getvalue

urlpatterns=[
    path('',home,name='home'),
    path('msg/',getvalue,name='ms')
]
