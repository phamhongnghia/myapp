# Generated by Django 4.1 on 2022-09-03 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresume', '0007_technical_script_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailtechnical',
            name='tech_exp',
            field=models.FloatField(null=True),
        ),
    ]
