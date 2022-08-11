# fractal_explorer/explorer/views.py

# System libraries

# Third-party libraries

# Django modules
from django.views.generic import TemplateView

# Django apps

#  Current app modules


class ExplorerView(TemplateView):
    template_name = 'explorer/explorer.html'
