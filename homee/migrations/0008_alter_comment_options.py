# Generated by Django 5.2.4 on 2025-07-24 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homee', '0007_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
    ]
