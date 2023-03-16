from csk.views import *
from django.urls import path
app_name='csk'
urlpatterns=[
    path('msdhoni/',msdhoni,name='msdhoni'),
    path('kohli/',kohli,name='kohli'),
]
    