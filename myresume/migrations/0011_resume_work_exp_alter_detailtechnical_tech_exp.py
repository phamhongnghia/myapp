# Generated by Django 4.1 on 2022-09-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresume', '0010_alter_detailtechnical_tech_exp'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='work_exp',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='detailtechnical',
            name='tech_exp',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
