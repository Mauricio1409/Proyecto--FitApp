# Generated by Django 5.2 on 2025-04-08 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='altura',
            field=models.FloatField(blank=True, help_text='Altura en cm', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='edad',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='perfil/'),
        ),
        migrations.AddField(
            model_name='user',
            name='nivel_entrenamiento',
            field=models.CharField(choices=[('principiante', 'Principiante'), ('intermedio', 'Intermedio'), ('avanzado', 'Avanzado')], default='principiante', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='objetivo',
            field=models.CharField(blank=True, choices=[('ganar_masa', 'Ganar masa muscular'), ('perder_grasa', 'Perder grasa'), ('mantener', 'Mantener forma física')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='peso',
            field=models.FloatField(blank=True, help_text='Peso en kg', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
