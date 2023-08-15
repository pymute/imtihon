from django.db import models
from datetime import datetime


# Create your models here.
class avtorModel(models.Model):
    kitob_nomi = models.CharField(default='', max_length=15)
    janri = models.CharField(default='', max_length=15)
    sifati = models.CharField(max_length=13, default='')
    avtor = models.CharField(default='', max_length=15)
    yili = models.DateField(default='')
    def __str__(self) -> str:
        return self.kitob_nomi
    class Meta:
        db_table = 'kitob'
        
class avtoridModel(models.Model):
    avtor_ismi = models.CharField(default='', max_length=15)
    kitoblari = models.CharField(default='', max_length=15)
    avtor_familiyasi = models.CharField(max_length=13, default='')
    tugulgan_sana = models.DateField(default='')
    def __str__(self) -> str:
        return self.avtor_ismi

    class Meta:
        db_table = 'avtor'
