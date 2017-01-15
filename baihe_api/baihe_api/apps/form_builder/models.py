from django.contrib.postgres.fields import JSONField
from django.db import models


class BaiheForm(models.Model):
    name = models.CharField(max_length=128, unique=True)
    comment = models.TextField(null=True, blank=True)
    structure = JSONField()
    created = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class BaiheFormData(models.Model):
    user = models.ForeignKey('baihe_user.BaiheUser', null=True)
    data = JSONField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField()
