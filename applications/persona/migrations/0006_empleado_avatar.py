# Generated by Django 3.1.2 on 2020-11-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_empleado_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
