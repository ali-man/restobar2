from django.db import models


class ConfigSite(models.Model):
    logo_main = models.ImageField(verbose_name='Главный логотип', upload_to='images/config/', blank=True)
    site_name = models.CharField(verbose_name='Название сайта', max_length=100, blank=True)
    site_info = models.TextField(verbose_name='Описание сайта', blank=True)
    col_list_products = models.IntegerField(verbose_name='Коливество товаров в категориях', blank=True)
    phone_supports = models.CharField(verbose_name='Номер телефона службы поддержки', max_length=100, blank=True)
    price_list = models.FileField(verbose_name='Прайс-лист', upload_to='files/config/', blank=True)

    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self):
        return self.site_name


class Slider(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100, blank=True)
    image = models.ImageField(verbose_name='Картинка', upload_to='images/sliders/')
    link = models.URLField(verbose_name='Ссылка', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Картинка слайдера'
        verbose_name_plural = 'Слайдер'

    def __str__(self):
        return self.title
