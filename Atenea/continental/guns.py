
#!/usr/bin/env python3

import os



token = os.environ['TOKEN']
#Se refiere a la variable de entorno FLAG (lo que nos interesa)
botf = os.environ['FLAG']
#Define el prefijo que deben tener los comandos para interactuar con el bot (!).
bot = commands.Bot(command_prefix='!')

#Significa que el bot sólo aceptará mensajes en un entorno DM, es decir, privado.
@commands.dm_only()
#Es el comando que provocará una determinada respuesta en el bot. Se deduce que junto con el prefijo sería “!!”.
@bot.command(name='!')

#roll es el nombre de la función.
#async def es una función corutinaria que sirve para definir “grupos” (no me sale el nombre).
# : int convierte el argumento o  en un número entero.
async def roll(ctx, o: int):

	ans = [
		':man_shrugging:',
		'Para Bellum',
		'I once saw him kill three men in a bar... with a pencil',
		'Everything has got a price',
		'Guns. Lots Of Guns'
	]
#ctx=El contexto
#message=El mensaje que desencadena la ejecución del comando.
#author=El Miembro que envió el mensaje. Si el canal es privado o el usuario ha dejado el grupo, es un Usuario.
	u = ctx.message.author
#t=John en ASCII
	t = chr(74)+chr(111)+chr(104)+chr(110)
# object.__str__() = u.__str__(). Devuelve una representación “bonita”, que los humanos podamos entender fácilmente, de object.
#str.split() transforma una cadena de texto en una lista. Por ejemplo, si str = “apple#banana#cherry#orange", split() lo transformará en [“apple”, “banana”, “cherry”, “orange”].
#Entiendo que t, es decir, "John", debe estar integrado en u. En otras palabras, el usuario debe mandar "John"
	if t in u.__str__().split('#')[0] and o == 299 :
#Parece que está línea es la encargada de mandar la flag (botf).
#.send se encarga de devolver “||” botf “||” al usuario (u)
		await u.send("||"+botf+"||")

		no = datetime.datetime.now()

	else:

		await u.send(random.choice(ans))


