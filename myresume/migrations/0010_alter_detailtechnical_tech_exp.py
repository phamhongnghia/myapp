# Generated by Django 4.1 on 2022-09-03 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresume', '0009_alter_detailtechnical_tech_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailtechnical',
            name='tech_exp',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
