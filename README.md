# Escaneo de IPs maliciosas

Este proyecto de Python monitorea conexiones de red salientes y detecta conexiones potencialmente maliciosas, generando automaticamente un archivo blacklist.txt en el cual se encarga de colocar las IPs publicas maliciosas

---

## 🚀 ¿Qué hace?

- Detecta conexiones de red salientes desde tu equipo.
- Verifica si esas IPs son públicas y potencialmente sospechosas.
- Si se detecta una IP maliciosa (según criterios definidos), se registra:
  - En blacklist_public Descarga un listado sobre las IPs publicas maliciosas desde la url (https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt)
  - En blacklist.txt: listado acumulativo de IPs maliciosas detectadas dependiendo del listado blacklist_public

---

## 📁 Estructura del proyecto

- main.py: Script principal para iniciar el monitoreo. La funcion es obtener conexiones salientes activas
- monitor.py: Se utiliza para identificar a qué servidores está conectado tu equipo en tiempo real.
- checker_offline.py: Fverifica si una IP es mailiciosa descargando un listado a traves de https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt
- utils.py`: Abre el archivo blacklist en modo lectura/escritura, chequea que la ip que se desea agregar no se encuentre en el listado.
- requirements.txt: Dependencias necesarias para ejecutar el proyecto.
- .gitignore`: Archivos y carpetas ignoradas por Git.

---

## ⚙️ Instalación

## Creacion un entorno virtual

- python -m venv venv
- source venv/bin/activate  # Linux/macOS
- venv\Scripts\activate   # Windows

## Instalacion de dependencias

pip install -r requirements.txt

---

## ▶️ Uso

#Para poder ejecutar el script debemos iniciar main.py

En la consola podremos verificar todas las conexiones salientes hacia internet, una vez encontrada una IP publica maliciosa lo estara informando tanto en la consola como en el archivo llamado blacklist.txt


---

## 📦 Archivos generados

- `blacklist.txt`: IPs que fueron clasificadas como maliciosas.
- `blacklist_public.txt`: Descarga un listado sobre las IPs publicas maliciosas desde la url https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt

---

