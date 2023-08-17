# Generated by Django 4.2.4 on 2023-08-17 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('reminder_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'TODO Detail',
                'verbose_name_plural': 'TODO Details',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_message', models.CharField(max_length=1024)),
                ('is_done', models.BooleanField(default=False)),
                ('details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='todo.tododetail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'TODO',
                'verbose_name_plural': 'TODOs',
            },
        ),
    ]
