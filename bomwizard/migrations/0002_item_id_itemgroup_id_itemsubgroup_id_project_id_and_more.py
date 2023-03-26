# Generated by Django 4.1.7 on 2023-03-26 14:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bomwizard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemgroup',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemsubgroup',
            name='id',
            field=models.BigAutoField(auto_created=True, default=11, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='id',
            field=models.BigAutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storagearea',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storagelocation',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='itemgroup',
            name='group_id',
            field=models.CharField(default='00', max_length=10),
        ),
        migrations.AlterField(
            model_name='itemsubgroup',
            name='category_id',
            field=models.CharField(default='00', max_length=3),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.CharField(default='00', max_length=10),
        ),
        migrations.AlterField(
            model_name='storagearea',
            name='storage_area_id',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='storagelocation',
            name='storage_location_id',
            field=models.CharField(max_length=10),
        ),
    ]
