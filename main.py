import random
# -- Puntuación --
score = random.randint(0, 10)

print ("Bienvenido a mi trivia sobre ajedrez")
print ("Pondremos a prueba tus conocimientos")
print ("Comenzarás con: ", score, "puntos")

name = input ("Ingresa tu nombre: ")
print ("\n Hola,", name,", responde las siguientes preguntas la letra de la alternativa que creas correcta y finalmente presiona 'Enter' para enviar tu respuesta \n")


# Pregunta 1 Rpta:D
print ("1) ¿Qué pieza de ajedrez puede hacer un movimiento en forma de L?")
print ("a) Peón")
print ("b) Reina")
print ("c) Alfil")
print ("d) Caballo")

response_1 = input("\n Tu respuesta: ")

# Validación
while response_1 not in ("a", "b", "c", "d"):
  response_1 = input("Debes ingresar a, b, c o d. Responde nuevamente: ")

if response_1 == "a":
  score -= 5
  print("Incorrecto!", name, "Pero estás cerca. Ánimos!")
elif response_1 == "b":
  score -= 5
  print("Incorrecto!", name, "Pero estás cerca. Ánimos!")
elif response_1 == "c":
  score -= 5
  print("Incorrecto!", name, "Pero estás cerca. Ánimos!")
else:
  score += 10
  print("Perfecto", name, "!")


# Pregunta 2 Rpta:C
print ("\n2) ¿Cómo se mueve el rey?")
print ("a) En diagonal, los espacios que quiera")
print ("b) En línea recta, solo un espacio")
print ("c) En la dirección que quiera, solo un espacio")
print ("d) En forma de L")

response_2 = input("\n Tu respuesta: ")

# Validación
while response_2 not in ("a", "b", "c", "d"):
  response_2 = input("Debes ingresar a, b, c o d. Responde nuevamente: ")

if response_2 == "c":
  score += 10
  print("Perfecto", name, "!")
else:
  print("Incorrecto!", name, "Pero estás cerca. Ánimos!")

# Pregunta 3 Rpta:A
print ("\n3) ¿Cómo se mueve la torre?")
print ("a) En línea recta, solo un espacio")
print ("b) En diagonal, los espacios que quiera")
print ("c) Hacia donde quiera, los espacios que quiera")
print ("d) En forma de L")

response_3 = input("\n Tu respuesta: ")

# Validación
while response_3 not in ("a", "b", "c", "d"):
  response_3 = input("Debes ingresar a, b, c o d. Responde nuevamente: ")

if response_3 == "a":
  score += 10
  print("Perfecto", name, "!")
else:
  print("Incorrecto!", name, "Pero estás cerca. Ánimos!")

# Pregunta 4 Rpta:B
print ("\n4) ¿Qué es el enroque?")
print ("a) Cuando el rey ya no puede moverse")
print ("b) Mover el rey y la torre en el mismo turno")
print ("c) Cuando un peón llega al otro extremo del tablero")
print ("d) Rendirse")

response_4 = input("\n Tu respuesta: ")

# Validación
while response_4 not in ("a", "b", "c", "d"):
  response_4 = input("Debes ingresar a, b, c o d. Responde nuevamente: ")

if response_4 == "b":
  score += 10
  print("Perfecto", name, "!")
else:
  print("Incorrecto!", name, "Pero estás cerca. Ánimos!")

# Pregunta 5 Rpta:B
print ("\n5) ¿Qué es el enroque?")
print ("a) Cuando el rey ya no puede moverse")
print ("b) Mover el rey y la torre en el mismo turno")
print ("c) Cuando un peón llega al otro extremo del tablero")
print ("d) Rendirse")

response_5 = input("\n Tu respuesta: ")

# Validación
while response_5 not in ("a", "b", "c", "d"):
  response_5 = input("Debes ingresar a, b, c o d. Responde nuevamente: ")

if response_5 == "b":
  score += 10
  print("Perfecto", name, "!")
else:
  print("Incorrecto!", name, "Pero estás cerca. Ánimos!")

# Mensaje final
print("Gracias", name, "por jugar mi trivia. Tu puntaje es: ", score, "puntos")