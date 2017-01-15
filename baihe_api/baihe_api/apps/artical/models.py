from django.db import models


class Artical(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    author = models.ForeignKey('baihe_user.BaiheUser', related_name='articals')
    read_count = models.PositiveIntegerField(default=0)
    share_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
