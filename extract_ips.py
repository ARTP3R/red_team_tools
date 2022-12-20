import re

# Abrimos el archivo
with open('ips.txt', 'r') as f:
  # Leemos el contenido del archivo
  content = f.read()

# Creamos una regex para coincidir con direcciones IP
ip_regex = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'

# Utilizamos la regex para extraer todas las direcciones IP del contenido del archivo
ips = re.findall(ip_regex, content)

# Creamos un conjunto para almacenar las direcciones IP únicas
unique_ips = set()

# Iteramos sobre las direcciones IP extraídas
for ip in ips:
  # Si la dirección IP no está en el conjunto, la añadimos y la mostramos por pantalla
  if ip not in unique_ips:
    unique_ips.add(ip)
    print(ip)
