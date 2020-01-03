from django.db import models

class Rubric(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='категория')

    class Meta:
        verbose_name_plural = 'категории'
        verbose_name = 'категория'
        ordering = ['name']

    def __str__(self):
        return self.name

class SubRubricOne(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Подкатегория')
    subrubric = models.ForeignKey(Rubric, max_length=30, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name_plural = 'Подкатегории'
        verbose_name = 'Подкатегория'
        ordering = ['name']

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='страна', unique=True)

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'
        ordering = ['name']

    def __str__(self):
        return self.name




class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='страна')
    name = models.CharField(max_length=30, db_index=True, verbose_name='область, край', unique=True)

    class Meta:
        verbose_name = 'область, край'
        verbose_name_plural = 'область, край'
        ordering = ['name']

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.PROTECT, verbose_name='область, край')
    name = models.CharField(max_length=50, db_index=True, verbose_name='город', unique=True)

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'
        ordering = ['name']

    def __str__(self):
        return self.name

class Bb(models.Model):

    KINDS = (
        (None, 'Выберите действие'),
        ('b', 'Куплю'),
        ('s', 'Продам'),
        ('c', 'Обменяю'),
    )

    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, verbose_name='Категория', null=True)
    subrubric = models.ForeignKey(SubRubricOne, on_delete=models.PROTECT, verbose_name='Подкатегория', null=True)
    title = models.CharField(max_length=100, verbose_name='Название товара')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='город', null=True)
    kind = models.CharField(max_length=1, choices=KINDS, null=True, verbose_name='Действие')

    class Meta:
        verbose_name_plural = 'объявления'
        verbose_name = 'объявление'
        ordering = ['-published']


