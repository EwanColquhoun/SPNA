# Generated by Django 4.0.3 on 2022-04-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_replied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='replied',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Yes')], default=False),
        ),
    ]