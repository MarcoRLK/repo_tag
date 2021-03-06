# Generated by Django 2.2.4 on 2019-08-24 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('github_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
                ('repos', models.ManyToManyField(to='app.Repository')),
            ],
        ),
        migrations.AddField(
            model_name='repository',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]
