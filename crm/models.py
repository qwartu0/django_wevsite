from tkinter.constants import CASCADE

from django.db import models

class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

# Create your models here.
class Orders(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return  self.order_name

    class Meta:
        verbose_name ='Заказ'
        verbose_name_plural ='Заказы'

class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Комментарии')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания комментария')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'