# Generated by Django 4.0.3 on 2022-04-02 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='replied',
            field=models.IntegerField(choices=[('No', 0), ('Yes', 1)], default=False),
        ),
    ]
