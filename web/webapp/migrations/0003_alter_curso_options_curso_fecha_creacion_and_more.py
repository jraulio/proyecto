# Generated by Django 4.2.5 on 2023-09-12 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_enregables_entregables'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'The Courses'},
        ),
        migrations.AddField(
            model_name='curso',
            name='fecha_creacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entregables',
            name='link',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
