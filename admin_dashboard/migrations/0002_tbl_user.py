# Generated by Django 5.1.3 on 2024-12-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=25)),
                ('Email', models.CharField(max_length=50)),
                ('Roles', models.CharField(max_length=30)),
                ('Status', models.CharField(max_length=15)),
            ],
        ),
    ]