# Generated by Django 4.2.9 on 2024-02-02 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_habit_habittracking_match_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habittracking',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='diaryimages/'),
        ),
    ]
