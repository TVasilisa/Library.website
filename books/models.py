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

class ReviewModel(models.Model):
    STARS = (
    ('⭐️', '⭐️'),
    ('⭐️⭐️', '⭐️⭐️'),
    ('⭐️⭐️⭐️', '⭐️⭐️⭐️'),
    ('⭐️⭐️⭐️⭐️', '⭐️⭐️⭐️⭐️'),
    ('⭐️⭐️⭐️⭐️⭐️', '⭐️⭐️⭐️⭐️⭐️')
    )

    choice_book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='reviewed_book')
    created_at = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=50, null=True)
    review_text = models.TextField(default= 'Рекомендую')
    stars = models.CharField(max_length=20, choices=STARS, default='⭐️⭐️⭐️⭐️⭐️')
    def __str__(self):
        return f'{self.stars} - {self.choice_book.title}'

