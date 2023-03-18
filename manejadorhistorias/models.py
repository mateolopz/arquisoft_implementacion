from django.db import models

class Historia(models.Model):
    id_historia = models.IntegerField()
    id_paciente = models.IntegerField()
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    edad = models.IntegerField()
    anio_nacimiento = models.IntegerField()
    edad = models.IntegerField()
    motivo = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return '%s %s %s' % (self.nombres, self.apellidos, self.fecha)

class Plan(models.Model):
    tipo = models.CharField(max_length=50)

class Antecedentes(models.Model):
    nombre = models.CharField(max_length=50)


