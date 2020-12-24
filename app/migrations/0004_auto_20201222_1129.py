# Generated by Django 3.1.2 on 2020-12-22 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201204_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.TextField(verbose_name='テキストファイル')),
            ],
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to='video/', verbose_name='動画ファイル'),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='file',
            field=models.ImageField(upload_to='image/'),
        ),
    ]