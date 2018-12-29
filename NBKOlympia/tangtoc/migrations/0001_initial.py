# Generated by Django 2.1.4 on 2018-12-29 14:37

from django.db import migrations, models
import tangtoc.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='Đáp án')),
                ('time_posted', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian trả lời')),
                ('question_number', models.IntegerField(verbose_name='Câu hỏi số')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Câu hỏi')),
                ('question_number', models.IntegerField(unique=True, verbose_name='Câu hỏi số')),
                ('file', models.FileField(blank=True, upload_to=tangtoc.models.question_directory_path, verbose_name='File đính kèm')),
                ('solution', models.CharField(max_length=255, verbose_name='Đáp án')),
            ],
        ),
    ]
