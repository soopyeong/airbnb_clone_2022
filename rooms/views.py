from django.views.generic import ListView
from . import models


class HomeView(ListView):

    """Homeview Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
