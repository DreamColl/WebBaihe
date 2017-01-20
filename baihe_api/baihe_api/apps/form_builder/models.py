# from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.db import models

FIELD_TYPE_CHOICES = ['text', 'phone', 'email', 'textarea',
                      'radio', 'select', 'checkbox', 'file', 'image']
VALIDATION_CHOICES = ['max_length', 'min_length']


class BaiheForm(models.Model):
    name = models.CharField(max_length=128, unique=True)
    comment = models.TextField(null=True, blank=True)
    # structure = JSONField()
    created = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class FormField(models.Model):
    form = models.ForeignKey(BaiheForm, related_name='fields')
    order = models.PositiveSmallIntegerField()
    field_type = models.ChoiceField(choices=FIELD_TYPE_CHOICES)
    label_name = models.CharField(max_length=100)
    placeholder = models.CharField(max_length=100, default='', blank=True, null=True)
    choices = models.CharField(default='', blank=True, null=True)
    default = models.CharField(max_length=100, default='', blank=True, null=True)
    required = models.BooleanField(default=False)


class BaiheFormData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    # data = JSONField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField()


class FormData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    form = models.ForeignKey(BaiheForm, related_name='datas')
    field = models.ForeignKey(FormField, related_name='data')
