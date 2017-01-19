from django.contrib import admin
from baihe_api.apps.form_builder.models import BaiheForm, BaiheFormData


@admin.register(BaiheForm)
class FormAdmin(admin.ModelAdmin):
    pass


@admin.register(BaiheFormData)
class FormDataAdmin(admin.ModelAdmin):
    pass
