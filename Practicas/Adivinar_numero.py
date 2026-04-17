import random
numero = random.randint(1,50)
intentos = 5

for intento in range(1, intentos + 1):
  try:
    intent = int(input(f"Intento {intento}/{intentos}. Adivina el numero: "))
    
    if intent == numero:
      print(f"{intent}: Adivinaste en {intento} intentos!")
      break
    elif intent < numero:
      print(f"{intent}: El numero es mayor")
    else:
      print(f"{intent}: El numero es menor")
  except ValueError:
    print("Error: Ingresa un numero valido")
else:
  print(f"Perdiste. El numero era: {numero}")