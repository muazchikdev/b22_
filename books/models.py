from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100,verbose_name = "Название жанра")
    image = models.ImageField(upload_to='genres/',verbose_name = "Изображения жанра")
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=200,verbose_name = "Имя автора")
    birth_date = models.DateField(verbose_name = "Дата рождения")
    death_date = models.DateField(blank=True, null=True,verbose_name = "Дата смерти")
    biography = models.TextField(verbose_name = "Биография")
    image = models.ImageField(upload_to='authors/',verbose_name = "Фото автора")


    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.full_name


class Book(models.Model):
    PART_CHOICES = [
        (1, 'Часть 1'),
        (2, 'Часть 2'),
        (3, 'Часть 3'),
    ]

    title = models.CharField(max_length=200,verbose_name = "Название книги")
    description = models.TextField(verbose_name = "коминтарий")
    pages = models.PositiveIntegerField(verbose_name = "Страницы  книги")
    part = models.IntegerField(choices=PART_CHOICES,verbose_name = "Части книги")
    pdf_file = models.FileField(upload_to='books_pdf/',verbose_name = "pdf файл книги")
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE,related_name='books',verbose_name = "Жанр")
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books',verbose_name = "Автор")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name = "Дата создание")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


    def __str__(self):
        return self.title
    
