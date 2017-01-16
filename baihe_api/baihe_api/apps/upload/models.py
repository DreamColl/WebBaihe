from django.db import models


class BaseFileModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class FileModel(BaseFileModel):
    upload = models.FileField(upload_to='files/%Y/%m/%d/')


class ImageModel(BaseFileModel):
    upload = models.ImageField(upload_to='images/%Y/%m/%d/')
