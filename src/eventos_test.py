from eventos import *
def test_es_dia_no_laborable():
    assert es_dia_no_laborable(2026-10-7) == False
    assert es_dia_no_laborable(2026-10-10) == True
    assert es_dia_no_laborable(2026-1-1) == True

def test_calcular_siguiente_valida():
    assert calcular_siguiente_valida(fecha_anterior=(2026-10-7),intervalo_dias=1)
    assert calcular_siguiente_valida(fecha_anterior=(2026-10-7),intervalo_dias=3)

planificar_eventos(fecha_inicio = date(2026, 1, 1),intervalo_dias = 10,num_eventos = 5)