# Generated by Django 4.2.4 on 2023-08-15 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='avtorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitob_nomi', models.CharField(default='', max_length=15)),
                ('janri', models.CharField(default='', max_length=15)),
                ('sifati', models.CharField(default='', max_length=13)),
                ('avtori', models.CharField(default='', max_length=15)),
                ('yili', models.DateField(default='')),
            ],
            options={
                'db_table': 'avtor',
            },
        ),
    ]
