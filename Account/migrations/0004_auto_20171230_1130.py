# Generated by Django 2.0 on 2017-12-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('Account', '0003_useraccount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='UserAccount',
        ),
    ]
