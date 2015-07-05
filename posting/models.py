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
    text = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    image_file = models.ImageField(
        upload_to='posting/%Y/%m/%d',
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']
