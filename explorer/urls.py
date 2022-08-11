# fractal_explorer/explorer/urls.py

# System libraries

# Third-party libraries

# Django modules
from django.urls import path

# Django apps

#  Current app modules
from .views import ExplorerView

app_name = 'explorer'

urlpatterns = [
    path('', ExplorerView.as_view(), name='explorer'),
]
