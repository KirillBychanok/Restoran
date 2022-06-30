from django.db import models

# Create your models here.
class FeedBack(models.Model):

    name = models.CharField(verbose_name='Имя', max_length=20)
    email = models.EmailField('Почта')
    message = models.TextField('Отзыв')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class DishCategory(models.Model):
    name = models.CharField('Категория блюда', max_length = 20)
    slug = models.SlugField('URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория блюда'
        verbose_name_plural = 'Категории блюд'

class Dish(models.Model):
    title = models.CharField('Название', max_length=20)
    description = models.CharField('Описание', max_length=100)
    price = models.FloatField('Цена')
    cat = models.ForeignKey('DishCategory', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

class Portfolio(models.Model):
    title = models.CharField('Заголовок', max_length=20)
    image = models.ImageField('Картинка', upload_to='static/media')
    cat = models.ForeignKey('DishCategory', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'