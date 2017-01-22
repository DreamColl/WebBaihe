from django.core.management import BaseCommand
from django.db.transaction import atomic
from baihe_api.apps.form_builder.models import FIELD_TYPE_CHOICES, FieldType


class Command(BaseCommand):
    help = 'init support field types for form builder'

    @atomic
    def handle(self, *args, **options):
        for (type, name) in FIELD_TYPE_CHOICES:
            ft = FieldType(type=type, name=name)
            ft.save()
        self.stdout.write(self.style.SUCCESS('field type init succuss'))
