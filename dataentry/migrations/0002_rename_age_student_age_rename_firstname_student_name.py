# Generated by Django 5.1.3 on 2024-11-16 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='firstName',
            new_name='name',
        ),
    ]