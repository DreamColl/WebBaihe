from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone

from baihe_api.apps.form_builder.models import BaiheForm, FormField


class FieldsInline(admin.TabularInline):
    model = FormField
    extra = 1


class FormStatusListFilter(admin.SimpleListFilter):
    title = "表单状态"

    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        return (
            ('unstarted', '未开始'),
            ('started', '正在进行'),
            ('ended', '已结束'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'unstarted':
            return queryset.filter(start_time__gt=timezone.now())
        elif self.value() == 'started':
            return queryset.filter(start_time__lte=timezone.now(),
                                   end_time__gte=timezone.now())
        elif self.value() == 'ended':
            return queryset.filter(end_time__lt=timezone.now())


@admin.register(BaiheForm)
class FormAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment', 'start_time', 'end_time']
    list_filter = [FormStatusListFilter]
    search_fields = ['name']
    actions = ['export_form']

    inlines = [FieldsInline]

    def export_form(self, request, queryset):
        response = HttpResponse(content_type="application/json")
        return response
