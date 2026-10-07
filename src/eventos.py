from datetime import date

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
