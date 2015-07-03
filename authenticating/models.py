from django.db import models
from django.contrib.auth.models import User
import uuid


class Account(models.Model):
    """
    site specific extension of the builtin User model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User)
    handle = models.CharField(max_length=100)

    def __unicode__(self):
        return self.handle or self.user

    class Meta:
        verbose_name = 'Site Account'
        verbose_name_plural = 'Site Accounts'
