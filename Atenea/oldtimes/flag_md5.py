#!/usr/bin/env python3

# script para pasar a formato de entrega flag md5 de Atenea

import hashlib

import sys

import pyperclip

if len(sys.argv) == 2:
	hashmd5 = hashlib.md5()
	stexto = sys.argv[1]
	hashmd5.update(stexto.encode())
	result = "flag{" + hashmd5.hexdigest() + "}"
	print(result)
	pyperclip.copy(result)
	print(result + " COPIADO AL PORTAPAPELES. LISTO PARA PEGAR.")
else:
	print("error - introducir argumentos correctamente")
	print('ejemplo: ./flag_md5.py "texto a codificar"')
	

