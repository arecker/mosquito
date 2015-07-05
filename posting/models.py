from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from authenticating.models import Account
import uuid


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Account)
    title = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __unicode__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ['-timestamp']


class TextPost(Post):
    text = models.TextField()


class LinkPost(Post):
    url = models.URLField()


class ImagePost(Post):
    file = models.ImageField(upload_to='posting/%Y/%m/%d')
