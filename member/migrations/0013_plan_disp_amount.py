# Generated by Django 4.0.3 on 2022-05-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0012_alter_plan_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='disp_amount',
            field=models.IntegerField(default='0'),
        ),
    ]
