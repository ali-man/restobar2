from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from pytils.translit import slugify


class Category(MPTTModel):
    sort = models.IntegerField(verbose_name='№', default=0)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(verbose_name='Имя категории', max_length=50)
    image = models.ImageField(verbose_name='Изображение', upload_to='images/categories/', blank=True)
    desc = RichTextUploadingField(verbose_name='Описание', blank=True)
    slug = models.SlugField(verbose_name='Slug', max_length=50, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    class MPTTMeta:
        order_insertion_by = ['name']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = str(self.id) + '-' + slugify(self.name)
            self.save(update_fields=['slug'])

    def __str__(self):
        if self.parent:
            text = '----' + self.name
        else:
            text = '' + self.name
        return text


class Manufacturer(models.Model):
    icon = models.ImageField(verbose_name='Изображение', upload_to='icons/manufacturers/')
    name = models.CharField(verbose_name='Производитель', max_length=50)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name


class Country(models.Model):
    icon = models.ImageField(verbose_name='Изображение', upload_to='icons/countries/')
    name = models.CharField(verbose_name='Страна', max_length=50)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название', max_length=250)

    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель', on_delete=models.PROTECT, null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name='Страна производителя', on_delete=models.PROTECT, null=True, blank=True)

    price = models.DecimalField(verbose_name='Цена', decimal_places=0, max_digits=12)
    new_price = models.DecimalField(verbose_name='Скидочная цена', decimal_places=0, max_digits=12, null=True, blank=True)
    leasing_price = models.DecimalField(verbose_name='Цена при покупке в лизинг', decimal_places=0, max_digits=12, null=True, blank=True)

    serving = models.IntegerField(verbose_name='Порций', null=True, blank=True)
    types_drinks = models.IntegerField(verbose_name='Видов напитков', null=True, blank=True)
    ingredients = models.IntegerField(verbose_name='Ингредиентов', null=True, blank=True)

    desc_short = RichTextUploadingField(verbose_name='Краткое описание')
    desc_full = RichTextUploadingField(verbose_name='Подробное описание')

    menu = RichTextUploadingField(verbose_name='Меню')
    shipping = models.ForeignKey('OtherInfo', verbose_name='Доставка и оплата', related_name='shipping', on_delete=models.PROTECT, null=True, blank=True)
    warranty = models.ForeignKey('OtherInfo', verbose_name='Гарантия', related_name='warranty', on_delete=models.PROTECT, null=True, blank=True)

    created_datetime = models.DateTimeField(verbose_name='Дата и время добавления', auto_now_add=True)
    status = models.BooleanField(verbose_name='Вывести на сайте', default=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    file = models.ImageField(verbose_name='Изображение', upload_to='images/products/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Картинка товара'
        verbose_name_plural = 'Картинки товаров'

    def __str__(self):
        return self.file.url


class Specification(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    key = models.CharField(verbose_name='Свойство', max_length=50)
    value = models.CharField(verbose_name='Значение', max_length=50)

    class Meta:
        verbose_name = 'Техническая характеристика'
        verbose_name_plural = 'Технические характеристики'

    def __str__(self):
        return self.key + ' ' + self.value


class OtherInfo(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    menu_name = models.CharField(verbose_name='Отображаемый заголовок', max_length=200, blank=True)
    desc = RichTextUploadingField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Доп. инфа товара'
        verbose_name_plural = 'Доп. инфа товаров'

    def __str__(self):
        return self.title