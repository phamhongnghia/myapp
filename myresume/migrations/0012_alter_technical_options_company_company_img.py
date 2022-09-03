# Generated by Django 4.1 on 2022-09-03 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myresume', '0011_resume_work_exp_alter_detailtechnical_tech_exp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technical',
            options={'ordering': ['tech_name', 'tech_description', 'script_code']},
        ),
        migrations.AddField(
            model_name='company',
            name='company_img',
            field=models.ImageField(null=True, upload_to='resume-image'),
        ),
    ]