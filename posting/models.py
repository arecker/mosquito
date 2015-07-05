from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from authenticating.models import Account
import uuid


class PostManager(models.Manager):
    def all_with_comment_counts(self):
        return super(
            models.Manager,
            self
        ).annotate(
            comment_count=models.Count('comment_set')
        )


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Account)
    title = models.CharField(max_length=200)
    url = models.URLField(blank=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-timestamp']
