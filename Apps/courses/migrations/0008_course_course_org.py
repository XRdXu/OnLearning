# Generated by Django 3.2.16 on 2023-04-04 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_auto_20230328_2016'),
        ('courses', '0007_course_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.organizations', verbose_name='Organization'),
        ),
    ]
