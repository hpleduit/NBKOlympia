# Generated by Django 2.1.4 on 2018-12-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tangtoc', '0002_answer_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='round',
            field=models.CharField(choices=[('tangtoc', 'Tăng tốc'), ('vcnv', 'VCNV'), ('', 'Empty')], default='tangtoc', max_length=255, verbose_name='Vòng thi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='round',
            field=models.CharField(choices=[('tangtoc', 'Tăng tốc'), ('vcnv', 'VCNV')], default='tangtoc', max_length=255, verbose_name='Vòng thi'),
            preserve_default=False,
        ),
    ]
