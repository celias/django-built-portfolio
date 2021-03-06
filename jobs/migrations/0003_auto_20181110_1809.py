# Generated by Django 2.0.2 on 2018-11-10 18:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='link',
        ),
        migrations.AddField(
            model_name='job',
            name='github',
            field=models.URLField(db_index=True, default=django.utils.timezone.now, max_length=150, unique=True, verbose_name='Github'),
            preserve_default=False,
        ),
    ]
