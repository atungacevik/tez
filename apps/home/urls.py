from django.urls import path
from home.views import *

app_name = 'home'

urlpatterns = [
    path('anasayfa', IndexPageView.as_view(), name='index'),
    path('university/<pk>', UniversityPageView.as_view(), name='uni_detail'),
    path('department/<pk>', DepartmentPageView.as_view(), name='dep_detail'),
    path('otherPage', OtherPageView.as_view(), name='other_detail'),
    path('search', SearchView.as_view(), name='search'),
    path('suggestionTool', SuggestionToolView.as_view(), name='suggestion'),

]
