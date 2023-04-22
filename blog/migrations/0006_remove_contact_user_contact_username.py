# Generated by Django 4.1.7 on 2023-04-22 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.AddField(
            model_name='contact',
            name='username',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]
