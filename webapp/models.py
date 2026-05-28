from django.db import models


STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано'),
]


class Task(models.Model):
    description = models.TextField(verbose_name='Описание')
    details = models.TextField(verbose_name='Подробное описание', blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name='Статус'
    )
    due_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата выполнения'
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.description[:50]} [{self.get_status_display()}]'
