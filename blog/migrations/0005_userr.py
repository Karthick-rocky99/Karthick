# Generated by Django 3.0.7 on 2020-07-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_ess'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200, unique=True)),
                ('uname', models.TextField(max_length=200, unique=True)),
                ('email', models.TextField(max_length=200, unique=True)),
                ('psw', models.TextField(max_length=200, unique=True)),
                ('cpsw', models.TextField(max_length=200, unique=True)),
                ('cou', models.TextField(max_length=200, unique=True)),
            ],
        ),
    ]
