import os #Se importa el modulo que es la forma de interactuar con el sistema operativo
import requests #Se importa el modulo ya que es una libreria que realiza solicitudes HTTP. En este caso se utiliza para descargar el archivo de las blacklist desde la url

# Nombre del archivo donde se guardará la blacklist
BLACKLIST_FILE = "blacklist_public.txt" #Nombre del archivo donde se alojan la lista descargada

# URL desde donde se descarga la blacklist pública
BLACKLIST_URL = "https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt"


def download_blacklist_if_needed() -> None: #EL proposito de la funcion es descargar la blacklist solo si el archivo no exite
    """
    Descarga la lista negra pública desde la URL si el archivo local no existe.

    Esto evita descargar la lista innecesariamente en cada ejecución.
    """
    if not os.path.exists(BLACKLIST_FILE): #Comprueba que el archivo no existe
        print("⬇️ Descargando lista negra pública...") #Imprime en pantalla que se descargo el archivo

        try: #Se utiliza el bloque try para manejo d eerrores que puedan ocurrir durante la solicitud HTTP.
            response = requests.get(BLACKLIST_URL, timeout=10) #Realiza una solcitud HTTP a la URL de la lista negra limitando el tiempo de respuesta a 10 segundos
            response.raise_for_status() #Verifica que la solicitud de respuesta sea exitosa

            with open(BLACKLIST_FILE, "w") as file: #Abrir archivo para escritura
                file.write(response.text) #Escribe el conteido del archivo

            print("✅ Lista descargada correctamente.") #Imprime en consola que la lista fue descargada

        except requests.RequestException as error: #Si ocurre cualquier error relacionado con solicitud HTTP se captura con except
            print(f"❌ Error al descargar la blacklist: {error}") #Al producirse el error nos muestra en pantalla un mensaje de error


def is_ip_in_public_blacklist(ip: str) -> bool: #Definimos la funcion en el cual se recibe el argumento ip de tipo str(Cadena de texto) y devuelve un valor booleano (True o False)
    """
    Verifica si una dirección IP se encuentra en la lista negra descargada.

    Args:
        ip (str): Dirección IP que se desea comprobar.

    Returns:
        bool: True si la IP está en la blacklist, False si no.
    """
    if not os.path.exists(BLACKLIST_FILE): #Verificacion del archivo. Si el archivo no existe, se muestra un mensaje de advertencia y la función retorna False.
        print("⚠️ No se encontró el archivo de blacklist. Intente descargarlo primero.") #Imprime en pantalla que no se encontro el archivo
        return False

    try: #El bloque try permite manejar errores al leer el archivo.
        with open(BLACKLIST_FILE, "r") as file: #Se abre el archivo en modo lectura
            blacklist = {line.strip() for line in file} #Se crea un conjunto de blacklist que contiene las lineas del archivo y se eliminan espacios y saltos antes de agregar cada IP.

        return ip in blacklist #Verificacion de la IP se encuentre alojado en el archivo

    except IOError as error: #si ocurre un error al leer el archivo, se captura la excepcion
        print(f"❌ Error al leer {BLACKLIST_FILE}: {error}") #Nos imprime en pantalla un mensaje de error.
        return False #La funcion retorna a False
