# age = int(input('What is your age?\n'))
# ✅ ↓ CHANGE THE CODE BELOW TO ADD 10 TO AGE ↓ ✅

# age += 10

# print("Your age is: "+str(age))


# MAYORIA_EDAD = (18);
# edad_usuario = (15);
# if(edad_usuario >= MAYORIA_EDAD):
    #print("El usuario es mayor de edad")



# edad_usuario = int(input('Cual es tu edad?'))
        
# if edad_usuario >= 18:
#    print("El usuario es mayor de edad y puede aprender a conducir todos los vehículos");
# elif edad_usuario >= 16:
#     print("El usuario es menor de edad pero podrá conducir ciclomotores de hasta 125cc");
# elif edad_usuario >= 15:
#     print("El usuario es menor de edad pero podrá conducir ciclomotores de hasta 50cc")
# else:
#     print("El usuario es menor de edad")


# edad_usuario = (15);
        
# if(edad_usuario >= 18):
#     print("El usuario es mayor de edad y puede aprender a conducir todos los vehículos");
# elif (edad_usuario >= 16):
#     print("El usuario es menor de edad pero podrá conducir ciclomotores de hasta 125cc");
# elif (edad_usuario >= 15):
#     print("El usuario es menor de edad pero podrá conducir ciclomotores de hasta 50cc");
# else:
#     print("El usuario no puede conducir")


# CONTAR DEL 1 AL 10 CON WHILE
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# i = 1
# while i <=20:
#     print(i)
#     i += 1
# i = 1 
# while i <=30:
#   #print(i)
#    i += 1

#    #imprimir numeros pares con while
# i = 2 
# while i <=30:
#    #print(i)
#    i += 2 

# i = 3 
# while i <= 10:
#    print(i)
#    i += 3  

#SUMA DEL 1 AL 100 CON WHILE
# i = 1
# sum = 0
# while i <= 100:
#     sum += 1
#     i += 1
#     print(sum)

# i = 10
# while i <= 200:
#     print(i)
#     i += 10 

#SOLICITAR AL USUARIO UN NUMERO 0

# numero = 1
# while numero != 0:
#     numero = int(input("Escribe(0 para salir):"))
#     print(numero) 


# Definición de la función
def sumarEnteros(*numeros):
    resultado = 0
    print(numeros, type(numeros))
    for numero in numeros:
        resultado = resultado + numero

    
    print("El resultado de la suma es:", resultado)

sumarEnteros (1)
sumarEnteros (6,7,8)