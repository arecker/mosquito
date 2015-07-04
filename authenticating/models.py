from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from annoying.fields import AutoOneToOneField
import logging
import uuid


class Account(models.Model):
    """
    site specific extension of the builtin User model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = AutoOneToOneField(User)
    handle = models.CharField(max_length=100, default='anon')

    def __unicode__(self):
        return self.handle or self.user

    class Meta:
        verbose_name = 'Site Account'
        verbose_name_plural = 'Site Accounts'


class Invitation(models.Model):
    """
    A half account waiting for a handle and new password
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User)
    subject = models.CharField(
        max_length=120,
        default='You have been invited to something special ;)'
    )
    message = models.TextField()
    send_on_save = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        try:
            return self.user.get_full_name() or self.get_username()
        except:
            return str(self.id)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse(
            'authenticating.views.complete_invitation',
            args=[str(self.id)]
        )

    def save(self, *args, **kwargs):
        if self.send_on_save:
            try:
                logger = logging.getLogger()
                self.send_on_save = False
                EmailMessage(
                    self.subject,
                    render_to_string(
                        'registration/invitation_email.html',
                        {
                            'invitation': self,
                            'protocol': 'http',
                            'domain': 'mosquito.alexrecker.com'
                        }
                    ),
                    to=[self.user.email, ]
                ).send()
            except Exception as e:
                logger.error(
                    'Error sending invitation {0}: {1}'.format(
                        self.pk,
                        e
                    )
                )
        super(Invitation, self).save(*args, **kwargs)
