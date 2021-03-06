# Generated by Django 3.2.9 on 2022-02-24 06:36

from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=user.models.get_file_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=user.models.get_file_path)),
                ('product_image_2', models.ImageField(blank=True, null=True, upload_to=user.models.get_file_path)),
                ('product_image_3', models.ImageField(blank=True, null=True, upload_to=user.models.get_file_path)),
                ('product_image_4', models.ImageField(blank=True, null=True, upload_to=user.models.get_file_path)),
                ('small_description', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default,1=Hidden')),
                ('tag', models.CharField(max_length=150)),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keyword', models.CharField(max_length=150)),
                ('meta_description', models.TextField(max_length=550)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.category')),
            ],
        ),
    ]
