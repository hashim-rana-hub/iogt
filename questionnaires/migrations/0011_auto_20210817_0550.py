# Generated by Django 3.1.13 on 2021-08-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0010_auto_20210802_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizformfield',
            name='correct_answer',
            field=models.CharField(help_text='The correct answer/choice(s). For checkboxes: a pipe (|) separated list of choices. For checkbox: Either "on" or "off".', max_length=256, verbose_name='correct_answer'),
        ),
    ]
