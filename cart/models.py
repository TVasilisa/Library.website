from django.db import models
from books.models import BookModel

class CartModel(models.Model):
    PAYMENT_CHOICES = (
        ('Наличные', 'Наличные'),
        ("Перевод", "Перевод")
    )
    choice_book = models.ForeignKey(BookModel, verbose_name= 'Добавьте книгу в заказ', on_delete=models.CASCADE)
    address = models.CharField(max_length=100, verbose_name='Введите ваш точный адрес для доставки: ')
    phone_number = models.CharField(max_length=15, verbose_name='Введите номер телефона: ')
    payment = models.CharField(verbose_name='Укажите способ оплаты: ', max_length=15, choices=PAYMENT_CHOICES)

    def __str__(self):
        return f"Заказ на следующие позиции: {self.choice_book}, по адресу: {self.address}, способ оплаты: {self.payment}"


