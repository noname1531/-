from django.db import models

# Create your models here.
class Settings(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Загаловок"
    )
    descriptions = models.TextField(
        verbose_name="Описание сайта"
    )
    photo = models.ImageField(
        upload_to='logo/image',
        verbose_name="Фотография"
    )

    def __str__(self):
        return self.name

        class Meta:
            verbose_name = "Настройки"
            verbose_name_plural = "Настройки сайта"