from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from .fields import EncryptedField


class Provider(models.Model):
    "Configuration for OAuth provider."

    name = models.CharField(max_length=50)
    request_token_url = models.URLField(blank=True)
    authorization_url = models.URLField()
    access_token_url = models.URLField()
    profile_url = models.URLField(blank=True)
    key = EncryptedField(blank=True, null=True, default=None)
    secret = EncryptedField(blank=True, null=True, default=None)

    def __unicode__(self):
        return self.name

    @property
    def enabled(self):
        enabled.boolean = True
        return self.key is not None and self.secret is not None


class AccountAccess(models.Model):
    "Authorized remote service."

    identifier = models.CharField(max_length=255)
    service = models.ForeignKey(Provider)
    user = models.ForeignKey('auth.User', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, default=datetime.now)
    modified = models.DateTimeField(auto_now=True, default=datetime.now)    
    access_token = models.TextField(default='', blank=True)
    raw_data = models.TextField(default='', blank=True)

    class Meta(object):
        unique_together = ('identifier', 'service')

    def __unicode__(self):
        return '{0} {1}'.format(self.service, self.name)
