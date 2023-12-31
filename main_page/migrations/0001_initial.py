# Generated by Django 4.2.7 on 2023-11-22 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afisha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_manga', models.CharField(max_length=100)),
                ('update_data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='manga/')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('ВЫПУСКАЕТСЯ', 'ВЫПУСКАЕТСЯ'), ('ЗАВЕРШЁН', 'ЗАВЕРШЁН')], max_length=30)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RunString',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Enter your title')),
                ('description', models.TextField(verbose_name='Enter your description')),
            ],
            options={
                'verbose_name': 'Бегущую строку',
                'verbose_name_plural': 'Бегущие строки',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.URLField()),
            ],
        ),
    ]
