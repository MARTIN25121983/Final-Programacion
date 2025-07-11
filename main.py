import time #Se importa el modulo time para realizar pausas
from monitor import get_outgoing_connections #Se importa la funcion get_outgoing_connections desde el modulo monitor. Esta función detecta las conexiones salientes activas del sistema
from checker_offline import is_ip_in_public_blacklist, download_blacklist_if_needed # download_blacklist_if_needed: descarga una blacklist pública si no existe
##is_ip_in_public_blacklist: verifica si una IP está presente en esa blacklist.
from utils import add_to_blacklist # Importa add_to_blacklist, función que registra IPs maliciosas detectadas en el archivo blacklist.txt, si aún no estaban guardadas.

def main() -> None: #Define la funcion principal del script. None indica que no devuelve ningun valor
    """
    Función principal del monitor de red.

    Descarga la lista negra si es necesario, luego analiza continuamente
    las conexiones salientes del sistema. Si se detecta una IP maliciosa
    en la lista negra, se registra en el archivo 'blacklist.txt'.
    """
    print("🛡️ Iniciando monitor de red ") #Muestra el mensaje en consola que comenzo a ejecutarse

    # Descargar la lista negra si no existe localmente
    download_blacklist_if_needed()

    while True: #Inicia el bucle infinito
        # Obtener conexiones salientes activas
        connections = get_outgoing_connections() #llama la funcion get_outgoing_connection para obtener una lista de conexiones salientes activas.

        for ip, port in connections: #Recorre cada conexion encontrada
            print(f"🌐 Conexión saliente detectada: {ip}:{port}")  #Imprime en consola las conexiones detectadas indicando IP y puerto

            if is_ip_in_public_blacklist(ip): #verifica si la IP detectada aparece en la blacklist pública.
                print(f"⚠️ IP maliciosa detectada en lista pública: {ip}") #Imprime la ip maliciosa
                add_to_blacklist(ip) #Agrega la IP maliciosa en el archivo blacklist.txt

        time.sleep(5)  # Espera entre ciclos y se puede modificar. EL programa espera 5 segundos antes de volver a escanear


if __name__ == "__main__": #Este bloque hace que la función main() se ejecute solo si el script se corre directamente.
    main()