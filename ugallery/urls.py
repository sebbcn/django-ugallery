from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .views import (
    GalleryView, GalleryTagView, PhotoDeleteView,
    PhotoView, PhotosView, PhotosTagView,
    PhotoCreateView, TagSearchView, AllTagsView)

urlpatterns = patterns(
    '',
    url(r'^$', GalleryView.as_view(), name='gallery'),
    url(r'^(?P<page>[0-9]*)/$', PhotosView.as_view(), name='photos'),

    url(r'^tag/(?P<tag_slug>[a-z-_0-9]*)/$',
        GalleryTagView.as_view(), name='gallery-tagged'),
    url(r'^tag/(?P<tag_slug>[a-z-_0-9]*)/(?P<page>[0-9]*)/$',
        PhotosTagView.as_view(), name='gallery-tagged-paginated'),
    
    url(r'^tags/$', AllTagsView.as_view(), name='gallery-all-tags'),
    url(r'^tags/search/$', TagSearchView.as_view(), name='gallery-search'),
    
    url(r'^photo/(?P<pk>[0-9]*)/$',
        PhotoView.as_view(), name='gallery-view-photo'),
    url(r'^photo/add/$',
        login_required(PhotoCreateView.as_view()), name='gallery-add-photo'),
    url(r'^photo/delete/(?P<pk>[0-9]*)/$',
        login_required(csrf_exempt(PhotoDeleteView.as_view())),
        name='gallery-del-photo'),
)
