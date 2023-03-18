from django.db import models

class Afiliacion(models.Model):
    id_afiliacion = models.IntegerField()
    id_paciente = models.IntegerField()
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return '%s %s %s' % (self.nombres, self.apellidos, self.fecha)

class Eps(models.Model):
    nombre = models.CharField(max_length=50)
    id_EPS = models.IntegerField()

class Ips(models.Model):
    nombre = models.CharField(max_length=50)
    id_IPS = models.IntegerField()

class ConsultaMedica(models.Model):
    tipo = models.CharField(max_length=50)
    id_paciente = models.IntegerField()
    id_medico = models.IntegerField()
    id_IPS = models.IntegerField()