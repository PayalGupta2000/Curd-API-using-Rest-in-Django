# Generated by Django 4.0.3 on 2022-09-25 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curdapi', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]
