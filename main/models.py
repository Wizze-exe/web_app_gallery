from django.db import models


# Create your models here.
class Arts(models.Model):
    title = models.CharField('Название', max_length=50, null=False)
    description = models.CharField('Автор', max_length=50, null=False)
    price = models.CharField('Цена', max_length=50, null=False)
    art = models.ImageField(null=False, upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Картина'
        verbose_name_plural = 'Картины'
