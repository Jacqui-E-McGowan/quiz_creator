# Generated by Django 2.2 on 2021-02-19 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_admin', '0002_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='message',
            field=models.TextField(null=True),
        ),
    ]