# Generated by Django 3.2.3 on 2021-05-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data', models.DateField()),
                ('status', models.IntegerField(choices=[(1, 'A fazer'), (2, 'Fazendo'), (3, 'Concluido')])),
            ],
        ),
    ]
