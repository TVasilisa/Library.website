from django.db import models


class BookModel(models.Model):
    GENRE_CHOICES = (
        ('FICTION', 'FICTION'),
        ('NONFICTION', 'NONFICTION'),
        ('FANTASY', 'FANTASY'),
    )
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите обложку книги')
    title = models.CharField(max_length=100, verbose_name="Укажите название книги")
    description = models.TextField(max_length=500, verbose_name='Добавьте описание к книге', blank=True)
    price = models.PositiveIntegerField(verbose_name='Укажите цену', default=300)
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    email = models.CharField(max_length=100, blank=True, verbose_name='Укажите почту автора')
    author = models.CharField(max_length=100, verbose_name='Укажите автора')
    review = models.URLField(verbose_name='Ссылка на краткую аннотацию о книге', blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
