# Generated by Django 3.2 on 2021-06-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_selfie', models.ImageField(default='static/query/1.jpg', upload_to='static/query')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Image',
                'db_table': 'image',
            },
        ),
    ]
