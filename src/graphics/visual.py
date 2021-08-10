from enum import Enum

class Visual(Enum):
    # General
    LIMPIAR = 'limpiar'

    # Configuracion
    PEDIR_ORDEN = 'pedir_orden'
    FALLO_ORDEN = 'fallo_orden'

    # Batalla
    CONTINUAR = 'continuar'
    TURNO = 'turno'
    VICTORIA = 'victoria'
    MAPA = 'mapa'
    TOCADO = 'tocado'
    AGUA = 'agua'
    COMIENZO = 'comienzo'

    # Bautizo
    PEDIR_NOMBRE = 'pedir_nombre'
    FALLO_NOMBRE = 'fallo_nombre'

