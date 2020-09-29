from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from frager.views.category_view import CategoryList
from frager.views.category_view import CategoryDetail

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>', CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)