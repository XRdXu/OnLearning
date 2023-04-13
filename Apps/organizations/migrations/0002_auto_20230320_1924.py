# Generated by Django 3.2.16 on 2023-03-20 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructors',
            options={'verbose_name': 'Instructors', 'verbose_name_plural': 'Instructors'},
        ),
        migrations.AlterModelOptions(
            name='organizations',
            options={'verbose_name': 'Organizations', 'verbose_name_plural': 'Organizations'},
        ),
        migrations.AlterField(
            model_name='instructors',
            name='image',
            field=models.ImageField(default='', upload_to='teacher/%Y/%m', verbose_name='profile photo'),
        ),
        migrations.AlterField(
            model_name='instructors',
            name='points',
            field=models.CharField(default='', max_length=50, verbose_name='characteristic'),
        ),
        migrations.AlterField(
            model_name='instructors',
            name='work_company',
            field=models.CharField(default='', max_length=50, verbose_name='company'),
        ),
        migrations.AlterField(
            model_name='instructors',
            name='work_position',
            field=models.CharField(default='', max_length=50, verbose_name='position'),
        ),
        migrations.AlterField(
            model_name='organizations',
            name='address',
            field=models.CharField(default='', max_length=150, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='organizations',
            name='desc',
            field=models.TextField(default='', max_length=10, verbose_name='Description'),
        ),
    ]