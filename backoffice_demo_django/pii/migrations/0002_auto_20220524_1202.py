# Generated by Django 3.2.13 on 2022-05-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pii', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(blank=True, null=True)),
                ('last_name', models.TextField(blank=True, null=True)),
                ('phone', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('eu', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pii',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
