# Generated by Django 3.0 on 2019-12-12 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20191210_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
