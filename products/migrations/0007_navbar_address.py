# Generated by Django 4.0.2 on 2022-02-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_footer_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='address',
            field=models.CharField(default='erfan', max_length=2083),
            preserve_default=False,
        ),
    ]
