# Generated by Django 4.2.5 on 2023-09-13 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_curso_options_curso_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entregables',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='profesion',
            new_name='materia',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='contraseña',
            field=models.CharField(default=2252, max_length=50),
            preserve_default=False,
        ),
    ]
