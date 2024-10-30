# Generated by Django 5.1.2 on 2024-10-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryhello', '0004_enrollment_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'abc_table',
                'ordering': ['-name'],
            },
        ),
    ]
