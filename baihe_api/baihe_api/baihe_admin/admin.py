from django.contrib import admin
from django.utils import timezone
from django.shortcuts import reverse

from baihe_api.apps.form_builder.models import BaiheForm, FormField
from baihe_api.apps.artical.models import Artical


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
    list_display = ['name', 'comment',
                    'start_time', 'end_time', 'export_excel']
    list_filter = [FormStatusListFilter]
    search_fields = ['name']

    inlines = [FieldsInline]

    def export_excel(self, obj):
        url = reverse('baiheform-export', kwargs={'pk': obj.pk})
        return url


admin.site.register(Artical)
