from django.views.generic import ListView, DetailView

from getbnb.mixins import MenuItemMixin
from .models import Property


class RecentListingListView(MenuItemMixin, ListView):
    queryset = Property.objects.prefetch_related('photos').\
        filter(is_published=True)
    template_name = 'listing/list_view.html'
    context_object_name = 'rooms'
    menu_item = 'listings'


class ListingDetailView(MenuItemMixin, DetailView):
    queryset = Property.objects.prefetch_related('photos', 'owner').\
        filter(is_published=True)
    template_name = 'listing/detail_view.html'
    context_object_name = 'room'
    menu_item = 'listings'
