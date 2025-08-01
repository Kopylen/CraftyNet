# Generated by Django 5.2.4 on 2025-07-22 08:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='home',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='homee.categories'),
        ),
        migrations.AddField(
            model_name='home',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='homee.tagpost'),
        ),
        migrations.AddIndex(
            model_name='home',
            index=models.Index(fields=['-time'], name='homee_home_time_dbf39d_idx'),
        ),
    ]
