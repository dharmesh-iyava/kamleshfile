# Generated by Django 3.0.6 on 2020-06-20 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_userdetail_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='tag',
            field=models.CharField(choices=[('s', 'shirt'), ('t', 't-hirt'), ('j', 'jeans')], max_length=1),
        ),
    ]
