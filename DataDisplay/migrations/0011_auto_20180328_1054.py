# Generated by Django 2.0.2 on 2018-03-28 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataDisplay', '0010_auto_20180328_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline_images',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
