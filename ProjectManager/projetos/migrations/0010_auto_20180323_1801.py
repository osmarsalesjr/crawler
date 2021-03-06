# Generated by Django 2.0 on 2018-03-23 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projetos', '0009_projeto_membros'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='projeto',
            name='administrador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='administradores', to='projetos.Perfil'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='membros',
            field=models.ManyToManyField(through='projetos.Usuario_Projeto', to='projetos.Perfil'),
        ),
        migrations.AlterField(
            model_name='usuario_projeto',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='projetos.Perfil'),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
