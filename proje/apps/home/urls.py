from django.urls import path
from home.views import *

app_name = 'home'

urlpatterns = [
    path('<pk>', UniversityPageView.as_view(), name='uni_detail'),
]
