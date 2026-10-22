###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
print("\nExercici 1:")
numero = 10
while numero >= 1:
  print(numero)
  numero -= 1
# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
num=1
suma_parells=0
while num <=20:
    if num%2==0:
        suma_parells+=num
   num+=1

print(f"La suma de parells és {suma_parells}")     
# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
enter_positiu=int(intput("Introdueix un enter positiu: "))
factorial=1
comptador=1
while comptador<=enter_positiu:
    factorial*=comptador
    comptador+=1
print(f"El factorial de {enter_positiu} és {factorial}")

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

contrasenya = input("Introdueix una contrasenya: ")

while len(contrasenya) < 8:
    print("La contrasenya ha de tenir almenys 8 caràcters. Torna-ho a provar.")
    contrasenya = input("Introdueix una contrasenya: ")

print("Contrasenya vàlida")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
num=int(intput("Introdueix un numero: "))
multiplicador=1
while multiplicador <=10:
    resultat=num*multiplicador
    print(f"¨{num}*{multiplicador}={resultat}")
    multiplicador+=1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
n=int(intput("Introdueix un enter positiu: "))
numemero=2
while numero<=n:
    es_primer = True  # Assumim que el número és primer fins que es demostri el contrari
  divisor = 2
  while divisor * divisor <= numero:  # Optimitzem: no cal provar divisors fins a numero
    if numero % divisor == 0:
      es_primer = False  # Si trobem un divisor, no és primer
      break  # Sortim del bucle interior
    divisor += 1
  if es_primer:
    print(numero)

  numero += 1
