# Generated by Django 2.2.17 on 2020-11-18 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201118_0838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customtext',
            old_name='hgjghjhjgjgjh',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='hgfhfgfhgfhgfhgf',
            new_name='body',
        ),
    ]
