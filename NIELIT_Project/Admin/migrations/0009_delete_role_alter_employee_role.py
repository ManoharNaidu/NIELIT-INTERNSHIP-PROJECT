# Generated by Django 4.2.3 on 2023-07-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_alter_employee_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(default='Trainee', max_length=1000),
        ),
    ]
