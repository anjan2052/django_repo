# Generated by Django 3.0.8 on 2020-08-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviereview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='review',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_year',
            field=models.DateField(blank=True, null=True),
        ),
    ]