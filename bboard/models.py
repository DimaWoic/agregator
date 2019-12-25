from django.db import models

class Rubric(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='категория')

    class Meta:
        verbose_name_plural = 'категории'
        verbose_name = 'категория'
        ordering = ['name']

    def __str__(self):
        return self.name


class Bb(models.Model):
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, verbose_name='Рубрика', null=True)
    title = models.CharField(max_length=100, verbose_name='Название товара')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'объявления'
        verbose_name = 'объявление'
        ordering = ['-published']

