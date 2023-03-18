from ..models import Historia
from datetime import datetime

def get_HistoriasUltimoLustro(procedimiento:str):
    anioActual = datetime.date.today().year
    diaActual = datetime.now().day
    mesActual = datetime.now().month
    historias = Historia.objects.exclude(fecha__gte=diaActual).filter(fecha__gte=datetime.date(anioActual,mesActual,diaActual)).filter(motivo__icontains=procedimiento)
    return historias

def get_historias():
    queryset = Historia.objects.all()
    return (queryset)