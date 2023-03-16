from mi.views import *
from django.urls import path
app_name='mi'
urlpatterns=[
    path('rohith/',rohith,name='rohith'),
    path('sachin/',sachin,name='sachin'),
]
    