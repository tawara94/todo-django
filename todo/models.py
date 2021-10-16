from django.db import models


class Todo(models.Model):
    class Meta:
        db_table = 'todo_lists'

    id = models.AutoField(verbose_name='id', primary_key=True)
    title = models.CharField(
        verbose_name='title',
        max_length=32,
    )
    body = models.CharField(
        verbose_name='body',
        max_length=1024,
        null=True,
        blank=True,
    )
    scheduled_at = models.DateTimeField(
        verbose_name='scheduled_at',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name='created_at',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='updated_at',
        auto_now=True,
    )
