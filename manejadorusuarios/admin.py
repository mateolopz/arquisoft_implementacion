from django.contrib import admin
from .models import Medico
from .models import Paciente
from .models import PersonalSalud

admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(PersonalSalud)
