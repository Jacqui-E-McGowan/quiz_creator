# Generated by Django 2.2 on 2021-02-21 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_admin', '0007_auto_20210220_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
