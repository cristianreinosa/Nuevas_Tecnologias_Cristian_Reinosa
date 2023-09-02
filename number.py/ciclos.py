import random

vidas = 5

puntos = 0

# Si sale 0 pierde una vida 
# Si se genra cualquier otro numero dentro un rango establecido gana puntos

while vidas !=0:
    num = random.randint(0,9)
    
    if num !=0:
        puntos+=1
        print("Tienes ",puntos," puntos") 
    else:
        vidas -=1
        print("Tienes ",vidas," vidas") 
              