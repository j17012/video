# Generated by Django 3.1.2 on 2021-01-15 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210115_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label_info',
            name='char_red',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='label_info',
            name='char_yellow',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='label_info',
            name='human_char',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='label_info',
            name='man',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='label_info',
            name='pc_cahr',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='label_info',
            name='sec',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='label_info',
            name='white_board',
            field=models.IntegerField(null=True),
        ),
    ]