from datetime import *

def es_dia_festivo(fecha: date) -> bool:
    """
    Verifica si una fecha corresponde a un día festivo recurrente (ignora el año).
    
    Parámetros:
        fecha (date): La fecha a verificar.
        
    Devuelve:
        bool: True si el mes y día coinciden con un festivo, False en caso contrario.
    """    
    dias_festivos = {
        (1, 1),    # Año Nuevo
        (1, 6),    # Día de Reyes
        (3, 19),   # San José
        (5, 1),    # Día del Trabajo
        (8, 15),   # Asunción de la Virgen
        (10, 12),  # Fiesta Nacional de España
        (11, 1),   # Todos los Santos
        (12, 6),   # Día de la Constitución
        (12, 8),   # Inmaculada Concepción
        (12, 25)   # Navidad
    }
    
    return (fecha.month, fecha.day) in dias_festivos
def es_dia_no_laborable(fecha: date)-> bool:
    if fecha.weekday() in (5,6) or es_dia_festivo(fecha):
        return True
    else:
        return False

def calcular_siguiente_valida(fecha_anterior, intervalo_dias):
    fecha_siguiente = fecha_anterior + timedelta(days=intervalo_dias)
    while es_dia_no_laborable(fecha_siguiente):
        fecha_siguiente=fecha_siguiente + timedelta(days=1)
    return fecha_siguiente

def planificar_eventos(fecha_inicio, intervalo_dias, num_eventos):
    fecha_evento = calcular_siguiente_valida(fecha_inicio,0)
    for i in range (1,num_eventos+1):
        print(f"Evento {i}: {fecha_evento}")
        fecha_evento = calcular_siguiente_valida(fecha_evento,intervalo_dias)
    

