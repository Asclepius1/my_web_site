from django.db import models

# Create your models here.
class ShmotAdd(models.Model):
    title = models.CharField(("Название"), max_length=50)
    image = models.ImageField(('Шмотье'), upload_to='media')
    sex = models.CharField(('Пол'), max_length=20)
    price = models.IntegerField('Цена')
    date = models.DateField('Дата выстовки')
    
    
    def __str__ (self):
        return self.title
    
    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'