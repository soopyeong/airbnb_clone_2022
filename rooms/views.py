from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render
from . import models


class HomeView(ListView):

    """Homeview Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", context={"room": room})
    except models.Room.DoesNotExist:
        raise Http404()
