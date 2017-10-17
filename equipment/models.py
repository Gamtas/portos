from django.urls import reverse
from django.db import models
from taggit.managers import TaggableManager


class Equipment(models.Model):
    type = models.CharField("Тип", max_length=100)
    serial_no = models.CharField("Заводской номер", max_length=30)

    tags = TaggableManager()

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        ordering = ('type',)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('equipment-detail', kwargs={'pk': self.pk})
