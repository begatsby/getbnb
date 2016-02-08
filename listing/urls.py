from django.conf.urls import url

from .views import RecentListView


urlpatterns = [
    url(r'recent/?$', RecentListView.as_view(), name='listing-recent')
]
