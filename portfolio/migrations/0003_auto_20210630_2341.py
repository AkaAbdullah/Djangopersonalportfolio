# Generated by Django 3.2.4 on 2021-06-30 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_aboutpage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='url',
            new_name='giturl',
        ),
        migrations.AddField(
            model_name='projects',
            name='videourl',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='profilepic',
            field=models.ImageField(upload_to='Uploads/'),
        ),
    ]