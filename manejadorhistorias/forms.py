from django import forms

class HistoriaForm(forms.Form):
    id_historia = forms.IntegerField()
    id_paciente = forms.IntegerField()
    apellidos = forms.CharField(max_length=50)
    nombres = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    anio_nacimiento = forms.IntegerField()
    motivo = forms.CharField(max_length=50)
    fecha = forms.DateField()  