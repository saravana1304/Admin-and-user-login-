# Generated by Django 4.1.6 on 2023-02-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Natural',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature_name', models.CharField(max_length=200)),
                ('nature_img', models.ImageField(upload_to='nat')),
                ('nature_country', models.CharField(max_length=200)),
            ],
        ),
    ]
