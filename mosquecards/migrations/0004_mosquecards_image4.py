# Generated by Django 2.0.2 on 2019-08-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosquecards', '0003_auto_20190819_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='mosquecards',
            name='image4',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
