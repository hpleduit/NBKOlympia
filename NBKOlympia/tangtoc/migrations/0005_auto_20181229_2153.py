# Generated by Django 2.1.4 on 2018-12-29 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tangtoc', '0004_auto_20181229_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_number',
            field=models.IntegerField(verbose_name='Câu hỏi số'),
        ),
    ]
