# Generated by Django 2.0 on 2020-05-17 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpackdb', '0018_auto_20200517_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='console',
            field=models.TextField(null=True),
        ),
    ]