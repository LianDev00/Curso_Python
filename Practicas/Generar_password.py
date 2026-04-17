import string
import random

def generar_password(longitud):
  mayus = string.ascii_uppercase
  minus = string.ascii_lowercase
  nums = string.digits
  simbolos = string.punctuation
  todos = mayus + minus + nums

  password = [
    random.choice(mayus), 
    random.choice(minus), 
    random.choice(nums),
    random.choice(simbolos),
  ]

  for _ in range(longitud - 4):
    password.append(random.choice(todos))
    
  random.shuffle(password)
  return "".join(password)

try:
  longitud = int(input("Longitud: "))
  if longitud < 8:
    print("Se necesitan al menos 8 caracteres")
  else:
    print(f"Password generada: {generar_password(longitud)}")
except ValueError:
  print("Debe ser un numero")