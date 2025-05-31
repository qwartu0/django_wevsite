from django.db import models

# Create your models here.
class CmsSlider(models.Model):
    slide_img = models.ImageField(upload_to='sliderimg/')
    slide_title = models.CharField(max_length=200, verbose_name='Заголовок')
    slide_text = models.CharField(max_length=200, verbose_name='Текст')
    slide_css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS класс')

    def __str__(self):
        return self.slide_title

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'
