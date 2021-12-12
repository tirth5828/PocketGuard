# Generated by Django 4.0 on 2021-12-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_remove_extendeduser_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeduser',
            name='age',
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='adhaar_num',
            field=models.IntegerField(default=551, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='pan_num',
            field=models.IntegerField(default=7785, unique=True),
            preserve_default=False,
        ),
    ]
