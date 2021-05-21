from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('inputo',views.inputo,name='inputo'),
    path('inputacc',views.inputacc,name='inputacc'),
    path('playo',views.playo,name='playo')
]