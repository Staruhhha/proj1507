from django.db import models
from django.urls import reverse, reverse_lazy

MAX_LENGTH_CHARFIELD = 100

class Supplier(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHARFIELD, verbose_name='Название поставщика')
    agent_firstname = models.CharField(max_length=MAX_LENGTH_CHARFIELD, verbose_name='Фамилия агента')
    agent_name = models.CharField(max_length=MAX_LENGTH_CHARFIELD, verbose_name='Имя агента')
    patronymic_name = models.CharField(max_length=MAX_LENGTH_CHARFIELD, blank=True,  verbose_name='Отчество агента')
    agent_telephone = models.CharField(max_length=MAX_LENGTH_CHARFIELD,  verbose_name='Телефон представителя')
    address =  models.CharField(max_length=MAX_LENGTH_CHARFIELD,  verbose_name='Адрес компании')

    def __str__(self):
        return f"{self.name} {self.agent_firstname} {self.agent_telephone}"

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Supply(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name='Поставщик')
    product = models.ManyToManyField('MusicInstrument', through='Pos_supply', verbose_name='Музыкальный инструмент')

    def __str__(self):
        return f"{self.pk}-{self.supplier.name}"

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'

class Pos_supply(models.Model):
    supply = models.ForeignKey(Supply, on_delete=models.PROTECT, verbose_name='Поставка')
    product = models.ForeignKey('MusicInstrument', on_delete=models.PROTECT, verbose_name='Музыкальный инструмент')

    count = models.PositiveIntegerField(verbose_name='Кол-во книг')

    def __str__(self):
        return f"{self.product.name}:{self.count} {self.supply}"

    class Meta:
        verbose_name = 'Позиция поставки'
        verbose_name_plural = 'Позиции поставки'


class Order(models.Model):
    MAGAZINE = 'MG'
    COURIER = 'CR'
    PICKUPPOINT = 'PP'

    DELIVERY_TYPE = [
        (MAGAZINE, 'Самовывоз'),
        (COURIER, 'Курьер'),
        (PICKUPPOINT, 'Точка выдачи заказов'),
    ]

    MAGAZINE = 'MG'
    COURIER = 'CR'
    PICKUPPOINT = 'PP'

    DELIVERY_TYPE = [
        (MAGAZINE, 'Самовывоз'),
        (COURIER, 'Курьер'),
        (PICKUPPOINT, 'Точка выдачи заказов'),
    ]

    customer_firstname = models.CharField(max_length=MAX_LENGTH_CHARFIELD, verbose_name='Фамилия клиента')
    customer_name = models.CharField(max_length=MAX_LENGTH_CHARFIELD, verbose_name='Имя клиента')
    customer_patronymic = models.CharField(max_length=MAX_LENGTH_CHARFIELD, blank=True, verbose_name='Отчество клиента')

    delivery_address = models.CharField(max_length=MAX_LENGTH_CHARFIELD, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=DELIVERY_TYPE, default=MAGAZINE, verbose_name='Тип доставки')

    commentary = models.TextField(blank=True, verbose_name='Комментарий к заказу')
    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания заказа')
    datetime_finish = models.DateTimeField(null=True, blank=True, verbose_name='Время завершения заказа')

    product = models.ManyToManyField('MusicInstrument', through='Pos_order', verbose_name='Музыкальный инструмент')

    def fio_customer(self):
        return f"{self.customer_firstname} {self.customer_name} {self.customer_patronymic}"

    def __str__(self):
        if self.customer_patronymic:
            return f"{self.pk} {self.customer_firstname} {self.customer_name[0]}.{self.customer_patronymic[0]}."
        return f"{self.pk} {self.customer_firstname} {self.customer_name[0]}."

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

        permissions = [
            ('change_delivery_type', 'Возможность изменить тип доставки'),
            ('can_finish_order', 'Возможность завершить заказ'),
        ]

class Pos_order(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    product = models.ForeignKey('MusicInstrument', on_delete=models.PROTECT, verbose_name='Музыкальный инструмента')

    count = models.PositiveIntegerField(verbose_name='Кол-во')
    discount = models.IntegerField(verbose_name='Скидка на позицию')

    def __str__(self):
        return f"{self.order} {self.product.name}"

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'


class Parametr(models.Model):
    name = models.CharField(unique=True, max_length=MAX_LENGTH_CHARFIELD, verbose_name='Характеристика')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристики товара'


class Pos_parametr(models.Model):
    parametr = models.ForeignKey(Parametr, on_delete=models.PROTECT, verbose_name='Характеристика')
    product = models.ForeignKey('MusicInstrument', on_delete=models.PROTECT, verbose_name='Книга')

    value = models.CharField(max_length=MAX_LENGTH_CHARFIELD, verbose_name='Значение характеристики')

    def __str__(self):
        return f"{self.product.name} | {self.parametr.name} : {self.value}"

    class Meta:
        verbose_name = 'Позиция характеристики'
        verbose_name_plural = 'Позиции характеристики'

class Category(models.Model):
    name = models.CharField(unique=True, max_length=MAX_LENGTH_CHARFIELD, verbose_name='Название категории')
    description = models.TextField(blank=True, verbose_name='Описании категории')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Brand(models.Model):
    name = models.CharField(unique=True, max_length=MAX_LENGTH_CHARFIELD, verbose_name='Название бренда')
    description = models.TextField(blank=True, verbose_name='Описании бренда')
    photo = models.ImageField(upload_to='images/brand', blank=True, verbose_name='Лого бренда')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class MusicInstrument(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHARFIELD, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=500, verbose_name='Цена')
    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    datetime_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, verbose_name='Изображение')
    is_exist = models.BooleanField(default=True, verbose_name='Существует?')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='Бренд')
    parametr = models.ManyToManyField(Parametr, through=Pos_parametr, verbose_name='Характеристики')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Музыкальный инструмент'
        verbose_name_plural = 'Музыкальный инструмент'