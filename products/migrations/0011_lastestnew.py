# Generated by Django 3.2.9 on 2022-03-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_page_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastestNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_adress', models.CharField(max_length=100)),
            ],
        ),
    ]
