# Generated by Django 2.1.3 on 2018-11-23 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20181123_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profle_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
