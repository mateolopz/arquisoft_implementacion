from django.db import models

class Medico(models.Model):
    id_medico = models.IntegerField()
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    edad = models.IntegerField()
    anio_nacimiento = models.IntegerField()
    especialidad = models.CharField(max_length=50)
    salario = models.IntegerField()

    def __str__(self):
        return '%s %s %s' % (self.nombres, self.apellidos, self.fecha)

class Paciente(models.Model):
    id_paciente = models.IntegerField()
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    edad = models.IntegerField()
    anio_nacimiento = models.IntegerField()

class PersonalSalud(models.Model):
    id_personal = models.IntegerField()
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    edad = models.IntegerField()
    anio_nacimiento = models.IntegerField()
    ocupacion = models.CharField(max_length=50)
    salario = models.IntegerField()

