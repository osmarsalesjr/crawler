# Generated by Django 2.0 on 2018-03-23 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0002_auto_20180323_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='membros',
            field=models.ManyToManyField(related_name='membros', through='projetos.Usuario_Projeto', to='projetos.Usuario'),
        ),
    ]
