#!/usr/bin/env python3
import requests
import time
from geoip2 import database

intervalo = 5 # segundos

reader = database.Reader('./GeoLite2-City.mmdb')

ip_anterior = ''

while True:
    # Petición GET a https://icanhazip.com/ para obtener la dirección IP pública
    respuesta = requests.get('https://icanhazip.com/')

    ip_actual = respuesta.text.strip()
    if ip_actual != ip_anterior:
        ip_anterior = ip_actual

        # API de geolocalización de MaxMind para obtener la información de ubicación
        try:
            ubicacion = reader.city(ip_actual)
            ciudad = ubicacion.city.name
            pais = ubicacion.country.name
            region = ubicacion.subdivisions.most_specific.name
            codigo_postal = ubicacion.postal.code
            latitud = ubicacion.location.latitude
            longitud = ubicacion.location.longitude

            print(f'Dirección IP: {ip_actual}')
            print(f'Ubicación: {ciudad}, {region}, {pais}, {codigo_postal}')
            print(f'Latitud: {latitud}, Longitud: {longitud}')

        except:
            print(f'No se pudo obtener la información de ubicación para la dirección IP {ip_actual}')

    time.sleep(intervalo)