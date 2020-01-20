# Generated by Django 3.0.2 on 2020-01-19 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default='img/profilepics/default-avatar.png', upload_to='img/profilepics/'),
        ),
    ]