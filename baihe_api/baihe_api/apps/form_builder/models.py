from django.conf import settings
from django.db import models

from baihe_api.common.models import ListField, PhoneField

FIELD_TYPE_CHOICES = [
    ('text', '单行文本'),
    ('textarea', '多行文本'),
    ('phone', '手机号码'),
    ('email', '电子邮箱'),
    ('date', '日期'),
    ('datetime', '日期时间'),
    ('radio', '单选'),
    ('checkbox', '多选'),
    ('select', '下拉框'),
    ('file', '文件'),
    ('image', '图片')
]


class FieldType(models.Model):
    type = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = '字段类型'
        verbose_name_plural = '字段类型'

    def __str__(self):
        return self.name


class BaiheForm(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name="名称")
    comment = models.CharField(
        max_length=128, null=True, blank=True, verbose_name="备注")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")

    class Meta:
        verbose_name = '表单'
        verbose_name_plural = '表单'

    def __str__(self):
        return self.name


class FormField(models.Model):
    form = models.ForeignKey(
        BaiheForm, related_name='fields', verbose_name="表单")
    order = models.PositiveSmallIntegerField(verbose_name="排序")
    field_type = models.ForeignKey(FieldType, verbose_name="字段类型")
    label_name = models.CharField(max_length=100, verbose_name="字段名称")
    placeholder = models.CharField(
        max_length=100, default='', blank=True, null=True, verbose_name="占位显示")
    choices = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="选项")
    default = models.CharField(
        max_length=100, default='', blank=True, null=True, verbose_name="默认值")
    required = models.BooleanField(default=False, verbose_name="必填")

    class Meta:
        verbose_name = '表单字段'
        verbose_name_plural = '表单字段'

    def __str__(self):
        return self.label_name


class BaiheFormData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, verbose_name="用户")
    form = models.ForeignKey(
        BaiheForm, verbose_name="表单")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = '表单数据'
        verbose_name_plural = '表单数据'

    def __str__(self):
        return self.form.name


class FormDataValue(models.Model):
    form_data = models.ForeignKey(
        BaiheFormData, related_name='data', verbose_name="表单数据")
    field = models.ForeignKey(
        FormField, related_name='data', verbose_name="字段")
    text = models.CharField(max_length=100, null=True, blank=True)
    textarea = models.TextField(null=True, blank=True)
    phone = PhoneField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    single_choice = models.CharField(max_length=100, null=True, blank=True)
    multiple_choice = ListField(null=True, blank=True)
    file = models.FileField(
        upload_to='files/%Y/%m/%d/', null=True, blank=True)
    image = models.ImageField(
        upload_to='images/%Y/%m/%d/', null=True, blank=True)

    def get_value(self):
        value = None
        if self.text:
            value = self.text
        elif self.textarea:
            value = self.textarea
        elif self.phone:
            value = self.phone
        elif self.email:
            value = self.email
        elif self.date:
            value = self.date
        elif self.datetime:
            value = self.datetime
        elif self.single_choice:
            value = self.single_choice
        elif self.multiple_choice:
            value = self.multiple_choice
        elif self.file:
            value = self.file
        elif self.image:
            value = self.image
        return value

    def __str__(self):
        return self.get_value()
