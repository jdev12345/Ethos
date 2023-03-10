# Generated by Django 3.1.2 on 2023-01-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_upload_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='audioname',
            field=models.CharField(default='DefaultName', max_length=500),
        ),
        migrations.AlterField(
            model_name='audio',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
