# Generated by Django 5.1.3 on 2024-12-05 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0003_permission_role_delete_user_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='Status',
            field=models.CharField(default='active', max_length=15),
        ),
    ]