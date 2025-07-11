def add_to_blacklist(ip: str) -> None: # La función add_to_blacklist recibe un argumento ip de tipo str (cadena de texto), que es la dirección IP que se quiere agregar al archivo blacklist.txt.
    """
    Agrega una dirección IP al archivo 'blacklist.txt' si aún no está presente.

    Esta función evita que se agreguen entradas duplicadas verificando 
    previamente el contenido del archivo.
    
    Args:
        ip (str): Dirección IP que se desea bloquear.
    """
    blacklist_path = "blacklist.txt" #Se define la variable blacklist_path que contiene el nombre del archivo donde se van a almacenar las direcciones IP bloqueadas (blacklist.txt).

    try: #Inicia un bloque de código que intenta ejecutar ciertas operaciones, y si ocurre algún error, lo manejará con el bloque except
        # Abrimos el archivo en modo lectura/escritura sin truncarlo
        with open(blacklist_path, "a+") as file: #asegura que el archivo se cierre automáticamente después de que se haya terminado de usar
            file.seek(0)  # Volvemos al inicio del archivo para leer su contenido
            # Creamos un conjunto con todas las IPs ya presentes, eliminando saltos de línea
            existing_ips = {line.strip() for line in file}# 

            # Solo escribimos la IP si no existe previamente
            if ip not in existing_ips:  #Verificacion de que no haya IPs duplicadas
                file.write(f"{ip}\n") #Si la IP no existe en el archivo, se agrega al final con un salto de línea (\n)

    except IOError as error: 
        # Capturamos errores relacionados al acceso del archivo
        print(f"❌ Error al acceder a {blacklist_path}: {error}") #Si ocurre un error se imprime el mensaje en pantalla
