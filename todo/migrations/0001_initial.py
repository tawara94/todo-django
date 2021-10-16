# Generated by Django 3.2.4 on 2021-06-18 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(max_length=32, verbose_name='title')),
                ('body', models.CharField(blank=True, max_length=1024, null=True, verbose_name='body')),
                ('scheduled_at', models.DateTimeField(blank=True, null=True, verbose_name='scheduled_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'db_table': 'todo_lists',
            },
        ),
    ]