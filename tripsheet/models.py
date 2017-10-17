from django.db import models
from django.urls import reverse
from equipment import models as equipment_models


class TripSheet(models.Model):
    equipment = models.ForeignKey(equipment_models.Equipment, verbose_name = 'Оборудование')
    working_hours_before = models.IntegerField("Рабочие часы в начале работы",)
    working_hours_after = models.IntegerField("Рабочие часы после работы",)
    work_end_time = models.DateTimeField("Работа зажешина",auto_now_add=True)
    notes = models.TextField("Заметки",blank=True, default='')

    class Meta:
        verbose_name = 'Рабочие часы'
        verbose_name_plural = 'Рабочие часы'
        ordering = ('-work_end_time',)

    def get_absolute_url(self):
        return reverse('tripsheet-detail', kwargs={'pk': self.pk})