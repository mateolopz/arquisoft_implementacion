from django.contrib import admin
from .models import Eps
from .models import Ips
from .models import Afiliacion
from .models import ConsultaMedica

admin.site.register(Eps)
admin.site.register(Ips)
admin.site.register(Afiliacion)
admin.site.register(ConsultaMedica)
