from django.conf.urls import url

from .views import RecentListingListView, ListingDetailView


urlpatterns = [
    url(r'recent/?$', RecentListingListView.as_view(), name='listing-recent'),
    url(r'(?P<pk>[0-9]+)/', ListingDetailView.as_view(), name='listing-detail')
]
