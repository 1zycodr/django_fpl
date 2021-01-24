# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField 
# from redactor.fields import RedactorField

class Document (models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    tags = models.CharField(max_length=250, verbose_name='Теги')
    file = models.FileField(upload_to='file/', verbose_name='Документ')

    class Meta:
        verbose_name = 'документ'
        verbose_name_plural = 'документы'

    def __str__(self):
        return self.title


class Purchase (models.Model):
    visits = models.IntegerField(default=0)
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    creation_date = models.DateTimeField(verbose_name='Дата создания')
    # description = models.TextField()
    
    description = RichTextUploadingField(blank=True, null=True, verbose_name='Описание')
    desc_file_title = models.CharField(max_length=250, verbose_name='Название файла описания')
    file_description = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='Pdf файл описания', default=None, related_name='ff')
    # file_description = models.FileField(upload_to='file/', verbose_name='Pdf файл описания')
    file_ur = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='Форма заявки для юр. лиц', default=None, related_name='qwf')
    # file_ur = models.FileField(upload_to='file/', verbose_name='Форма заявки для юр. лиц')
    file_fiz = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='Форма заявки для физ. лиц', default=None, related_name='aas')
    # file_fiz = models.FileField(upload_to='file/', verbose_name='Форма заявки для физ. лиц')  
    file_kwal = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='Форма сведений о квалификации', default=None, related_name='bs')
    # file_kwal = models.FileField(upload_to='file/', verbose_name='Форма сведений о квалификации')

    class Meta:
        verbose_name = 'закупка'
        verbose_name_plural = 'Закупки'

    def __str__(self):
        return self.title

class Category (models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name='Название')
    par_cat_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Родительская категория')

    class Meta: 
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name

class Region (models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name='Название')
    par_reg_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Родительский регион')

    class Meta:
        verbose_name = 'регион'
        verbose_name_plural = 'Регионы'
     
    def __str__(self):
        return self.name

class Asset (models.Model):
    state = models.BooleanField(default=True, verbose_name='Опубликовано', blank=True, null=True)
    visits = models.IntegerField(default=0, blank=True, null=True)
    title = models.CharField(max_length=250, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    # discription = models.TextField(verbose_name='Описание')
    # discription = RichTextField(blank=True, null=True, verbose_name='Описание')
    creation_date = models.DateTimeField(verbose_name='Дата создания', null=True)
    description = RichTextUploadingField(blank=True, null=True, verbose_name='Описание')
    price = models.CharField(verbose_name='Цена', max_length=250)
    min_price = models.IntegerField(verbose_name='Минимальная цена', null=True, blank=True)
    performance_date = models.DateTimeField(verbose_name='Дата проведения')
    location = models.TextField(verbose_name='Местоположение')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регион')
    bargaining_link = models.CharField(
        max_length = 250, 
        verbose_name = 'Ссылка на торги',
        blank = True
    )

    INCREASE = 'IN'
    DECREASE = 'DE'

    AS_TYPE_CHOICES = [
        (INCREASE, 'На повышение цены'),
        (DECREASE, 'На понижение цены'), 
    ]

    as_type = models.CharField(max_length=30, choices = AS_TYPE_CHOICES, verbose_name='Тип')
    image = models.ImageField(upload_to = 'img/', verbose_name='Фото')

    class Meta:
        verbose_name = 'актив'
        verbose_name_plural = 'Активы'
    
    def __str__(self):
        return self.title
    
class News (models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    image = models.ImageField(upload_to = 'img/', verbose_name='Фото', blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True, verbose_name='Описание')
    creation_date = models.DateTimeField(verbose_name='Дата создания')

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

class Leader (models.Model):
    full_name = models.CharField(max_length=250, verbose_name='Полное имя')
    position = models.CharField(max_length=250, verbose_name='Должность')
    description = RichTextUploadingField(blank=True, null=True, verbose_name='Информация')
    image = models.ImageField(upload_to = 'img/', verbose_name='Фото', null=True)

    class Meta:
        verbose_name = 'руководитель'
        verbose_name_plural = 'Руководители'

    def __str__(self):
        return self.full_name

class Results (models.Model):
    visits = models.IntegerField(default=0)
    creation_date = models.DateTimeField(verbose_name='Дата создания')
    title = models.CharField(max_length=250, verbose_name='Название')
    description = RichTextUploadingField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'итог'
        verbose_name_plural = 'Итоги'

    def __str__(self):
        return self.title

class Audit (models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    f1_title = models.CharField(max_length=50, verbose_name='Название файла 1')
    # file = models.FileField(upload_to='file/', verbose_name='Файл 1')
    file = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='Документ', default=None)
    f2_title = models.CharField(max_length=50, verbose_name='Название файла 2', null=True, blank=True)
    # file2 = models.FileField(upload_to='file/', verbose_name='Файл 2', null=True, blank=True)
    file2 = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='Документ', default=None, related_name='doc_2', null=True, blank=True)
    image = models.ImageField(upload_to = 'img/', verbose_name='Фоновая картинка', null=True)

    class Meta:
        verbose_name = 'внешний аудит'
        verbose_name_plural = 'Внешний аудит'

    def __str__(self):
        return self.title



class FinOtchet (models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    file = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name='Документ')
    image = models.ImageField(upload_to = 'img/', verbose_name='Фоновая картинка', null=True)

    class Meta:
        verbose_name = 'годовой отчёт'
        verbose_name_plural = 'годовые отчёты'

    def __str__(self):
        return self.title

class Page (models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    tags = models.TextField(verbose_name='Теги')
    link = models.CharField(max_length=250, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'страница'
        verbose_name_plural = 'страницы'

    def __str__(self):
        return self.title

class Directors (models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    photo = models.ImageField(upload_to = 'img/', verbose_name='Фото')
    position = models.CharField(max_length=200, verbose_name='Должность')
    description = RichTextUploadingField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'директор'
        verbose_name_plural = 'директоры'

    def __str__(self):
        return self.name

class Government (models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    photo = models.ImageField(upload_to = 'img/', verbose_name='Фото')
    position = models.CharField(max_length=200, verbose_name='Должность')
    # description = RedactorField(null=True,verbose_name='Описание')
    description = RichTextUploadingField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'член правления'
        verbose_name_plural = 'члены правления'

    def __str__(self):
        return self.name

