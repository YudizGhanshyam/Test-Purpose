# Generated by Django 4.0 on 2022-01-17 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_rename_studnet_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionregister',
            name='option1',
        ),
        migrations.RemoveField(
            model_name='questionregister',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='questionregister',
            name='option3',
        ),
        migrations.RemoveField(
            model_name='questionregister',
            name='option4',
        ),
        migrations.AddField(
            model_name='questionregister',
            name='Corrans',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionregister',
            name='Marks',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='questionregister',
            name='Option1',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionregister',
            name='Option2',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionregister',
            name='Option3',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionregister',
            name='Option4',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questionregister',
            name='question',
            field=models.CharField(max_length=200),
        ),
    ]