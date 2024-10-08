# Generated by Django 5.1.1 on 2024-09-26 20:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_coursefunction_usercoursehistory'),
        ('permissions', '0003_rename_subsector_usersectorpermissions_sector_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursefunction',
            name='function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='functions', to='permissions.function'),
        ),
    ]
