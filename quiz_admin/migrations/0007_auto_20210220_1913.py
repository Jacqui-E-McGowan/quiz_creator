# Generated by Django 2.2 on 2021-02-21 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_admin', '0006_auto_20210220_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
