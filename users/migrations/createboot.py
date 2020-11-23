from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import migrations


def add_bot(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))
    User.objects.create(
        email='financialboot@test.com',
        password=make_password('s3cr3tp4ssw0rd!'),
        username='Financial Boot',
    )


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(add_bot),
    ]
