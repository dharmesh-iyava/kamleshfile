# Generated by Django 3.0.6 on 2020-06-14 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_userdetail_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]
