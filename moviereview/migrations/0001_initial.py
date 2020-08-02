# Generated by Django 3.0.8 on 2020-08-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_year', models.DateTimeField()),
                ('poster', models.ImageField(blank=True, null=True, upload_to='posters/')),
            ],
        ),
    ]