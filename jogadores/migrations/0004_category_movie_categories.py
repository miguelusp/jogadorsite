# Generated by Django 4.2.6 on 2023-11-18 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogadores', '0003_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='jogador',
            name='categories',
            field=models.ManyToManyField(to='jogadores.category'),
        ),
    ]
