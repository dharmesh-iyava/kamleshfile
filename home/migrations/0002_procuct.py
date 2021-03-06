# Generated by Django 3.0.6 on 2020-06-05 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procuct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('tag', models.CharField(choices=[('S', 'Shirt'), ('T', 'T-Shirt'), ('J', 'Jeans')], max_length=1)),
                ('price', models.FloatField(blank=True, max_length=5, null=True)),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
            ],
        ),
    ]
