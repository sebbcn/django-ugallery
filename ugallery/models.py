from django.db import models
from taggit.managers import TaggableManager
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import generate_all_aliases


class Photo(models.Model):

    title = models.CharField(max_length=80)
    photo = ThumbnailerImageField(upload_to='photos', blank=True)
    date = models.DateTimeField(auto_now=False)
    tags = TaggableManager()
    
    class Meta:
    	db_table = 'gallery_photo'

    def __unicode__(self):

        return '%s - %s' % (self.title, self.photo)

    def save(self):

        generate_all_aliases(self.photo, True)
        super(Photo, self).save()
