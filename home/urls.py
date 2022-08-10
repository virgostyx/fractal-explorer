# project_name/app_module/file_name.py

# System libraries

# Third-party libraries

# Django modules
from django.urls import path

# Django apps

#  Current app modules
from .views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
