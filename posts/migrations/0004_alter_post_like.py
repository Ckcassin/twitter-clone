# Generated by Django 4.0.6 on 2022-08-09 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_image_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='like_count'),
        ),
    ]