from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Введите название категории"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Введите описание"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=70,
        verbose_name="Наименование",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Введите описание"
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите название категории",
        blank=True,
        null=True,
        related_name='products',
    )
    price = models.FloatField(verbose_name="Цена",help_text="Введите описание")
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создание записи",
        help_text="Укажите дату создания",
    )
    updated_at = models.DateField(
        blank=True, null=True, verbose_name="Дата последнего изменения"
    )

    manufactured_at = models.DateField(
        blank=True, null=True, verbose_name="Дата производства продукта"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "created_at", "updated_at"]

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок"
    )
    slug = models.SlugField(
        blank=True,
        null=True,
        max_length=150,
        unique=True,
        verbose_name="slug"
    )
    text = models.TextField(
        blank=True,
        null=True,
        verbose_name="Текст",
        help_text="Введите текст"
    )
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to='catalog/photo',
        verbose_name='Изображение',
        help_text='Выберите изображение'
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создание записи",
        help_text="Укажите дату создания",
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения"
    )
    viewed = models.IntegerField(
        default=0,
        verbose_name='Количество просмотров'
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title", "created_at", "updated_at"]

    def __str__(self):
        return self.title
