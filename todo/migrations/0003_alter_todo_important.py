# Generated by Django 4.0.5 on 2022-06-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_datecompleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]
