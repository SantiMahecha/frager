from django.urls import path, include

urlpatterns = [
    path('', include('categories_fragen.urls')),
]

