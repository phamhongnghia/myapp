# Generated by Django 4.1 on 2022-09-03 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresume', '0008_alter_detailtechnical_tech_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailtechnical',
            name='tech_exp',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
