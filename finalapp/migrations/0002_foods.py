# Generated by Django 4.2 on 2023-05-19 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('qty', models.IntegerField()),
                ('price', models.IntegerField()),
                ('f_image', models.ImageField(null=True, upload_to='image/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finalapp.category')),
            ],
        ),
    ]
