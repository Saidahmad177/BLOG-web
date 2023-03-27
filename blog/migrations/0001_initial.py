# Generated by Django 4.1.7 on 2023-03-27 18:14

from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/')),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
            ],
            options={
                'ordering': ['-publish_date'],
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
