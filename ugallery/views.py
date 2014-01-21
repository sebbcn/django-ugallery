
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy

from django.views.generic import View, TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from extra_views import ModelFormSetView

from taggit.models import Tag
from ugallery.models import Photo


class GalleryView(TemplateView):
    ''' returns an empty gallery page. '''

    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):

        context = super(GalleryView, self).get_context_data(**kwargs)
        context.update(dict(
            most_common_tags=Photo.tags.most_common()[0:7],
            load_url=reverse('gallery')))
        return context


class GalleryTagView(GalleryView):
    ''' returns an empty gallery page with tag filter. '''

    def get_context_data(self, **kwargs):

        context = super(GalleryTagView, self).get_context_data(**kwargs)
        tag_slug = context['tag_slug']
        tag = get_object_or_404(Tag, slug=tag_slug)
        context.update(dict(
            load_url=reverse('gallery-tagged', args=(tag_slug,)), tag=tag
        ))
        return context


class PhotosView(ListView):
    ''' Returns a number of photos through Ajax request '''

    paginate_by = 12
    queryset = Photo.objects.all().order_by('-date')
    template_name = 'photo_list.html'

    def get_context_data(self, **kwargs):

        context = super(PhotosView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        
        return context


class PhotosTagView(PhotosView):
    ''' Returns a number of photos related to a given tag through Ajax request '''

    def get_queryset(self):

        queryset = super(PhotosTagView, self).get_queryset()
        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug is None:
            return queryset
        return queryset.filter(tags__slug=tag_slug)
        

class PhotoView(DetailView):
    model = Photo
    template_name = 'photo_detail.html'


class PhotoCreateView(ModelFormSetView):
    model = Photo
    template_name = 'photo_form.html'
    extra = 20

    def get_queryset(self):
        return Photo.objects.none()


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('gallery')


class TagSearchView(View):

    def get(self, request, *args, **kwargs):

        slugs = Photo.tags.all()
        q = request.GET.get('q', None)
        if q:
            slugs = slugs.filter(slug__contains=q)
        
        slugs = slugs.order_by('slug').values_list('slug', flat=True)
        slugs = [s.replace('-', ' ') for s in slugs]
        return HttpResponse(json.dumps(slugs), content_type='application/json')


class AllTagsView(TemplateView):

    template_name = 'gallery_all_tags.html'

    def get_context_data(self, **kwargs):

        context = super(AllTagsView, self).get_context_data(**kwargs)
        context.update(dict(tags=Photo.tags.all().order_by('slug')))
        return context
