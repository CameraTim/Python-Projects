# Generated by Django 4.0.4 on 2022-05-10 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('courseNumber', models.IntegerField()),
                ('instructor', models.CharField(max_length=30)),
                ('duration', models.DecimalField(decimal_places=3, max_digits=10000)),
            ],
        ),
    ]