# Generated by Django 3.2.6 on 2021-10-21 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20211020_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='fish',
            name='toys',
            field=models.ManyToManyField(to='main_app.Toy'),
        ),
    ]