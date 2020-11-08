from django.db import models

# Create your models here.


class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['-name', 'short_name']  # ordena por orden alfabetico
        # no permita que se registra un atributos 2 veces
        unique_together = ('name', 'short_name')

    def __str__(self):
        return self.name + '-'+self.short_name
