from django.db import models
import datetime

# Create your models here.
class Adoptante(models.Model):
    run = models.CharField(primary_key=True, max_length=15, help_text="Rut del Adoptante")
    email = models.EmailField(help_text="Correo Electronico")
    nombre = models.CharField(max_length=100, help_text="Nombre y Apellido")
    fecha_nacimiento = models.DateField(default=datetime.date.today, help_text="Fecha de Nacimiento")
    telefono = models.IntegerField(help_text="Numero de Celular")
    region = models.CharField(max_length=100, help_text="Region")
    ciudad = models.CharField(max_length=100, help_text="Ciudad")
    opt=(('G', 'Casa con Patio Grande'),('P','Casa con Patio Pequeño'),('S','Casa sin patio'),('D','Departamento'))
    tipo_vivienda = models.CharField(max_length=1, choices=opt,default='Casa con Patio Grande', help_text="Tamaño de la Vivienda")

    def __str__(self):
        return"{0} {1}".format(self.nombre, self.run)
