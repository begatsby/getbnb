from django.views.generic import ListView

from .models import Property


class RecentListView(ListView):
    queryset = Property.objects.prefetch_related('photos').filter(is_published=True)
    template_name = 'listing/list_view.html'
    context_object_name = 'rooms'


class DetailView():
    pass
