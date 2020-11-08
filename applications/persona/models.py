from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id)+'-'+self.habilidad

class Empleado(models.Model):
    """
    Modelo para tabla empleado
    """
    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO'),
    )

    #Contador
    #Administrador
    #Economista
    #Otro
    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    full_name = models.CharField(
        'Nombres completos',
        max_length=50,
        blank=True
    )
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['last_name', 'first_name']#ordena por orden alfabetico


    def __str__(self):
        return str(self.id)+'-'+self.first_name +'-'+self.last_name

