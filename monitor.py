import psutil # Importa la biblioteca psutil, que permite acceder a la informacion de los procesos del sistema (CPU, memoria y conexiones de red)
from typing import List, Tuple 

def get_outgoing_connections() -> List[Tuple[str, int]]: #Definimos a la funcion donde devuelve una lista de tuplas y donde cada tupla contiene una IP (str) y un puerto (int)
    """
    Obtiene una lista de conexiones salientes activas (ESTABLISHED) en el sistema.

    Analiza todas las conexiones de red de tipo 'inet' (IPv4 e IPv6) y devuelve
    aquellas que están activas y poseen una dirección remota.

    Returns:
        List[Tuple[str, int]]: Lista de tuplas con IP y puerto de destino.
    """
    connections = psutil.net_connections(kind='inet') #Se utiliza para obtener todas las conexiones de red, filtrando conexiones IPV4 e IPV6
    outgoing = [] #Crea una lista vacía donde se almacenan las conexiones establecidas (IP y puerto de destino).

    for conn in connections: #Inicia el bucle que recorre cada conexion
        # Solo conexiones activas con dirección remota
        if conn.status == 'ESTABLISHED' and conn.raddr: #Filtra conexiones  que esten activas
            ip = getattr(conn.raddr, 'ip', None) # Extrae de forma segura la IP y el puerto del destino remoto.
            port = getattr(conn.raddr, 'port', None) #Extrae de forma segura el puerto del destino remoto.

            if ip and port: #Si ambos valores existen(ip y puerto) se guarda en la tupla en la lista outgoing
                outgoing.append((ip, port))

    return outgoing # Devuelve la lista completa de conexiones  activas detectadas.