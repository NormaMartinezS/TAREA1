print("Bienvenido a NORMASCORP")
while True:
    respuesta=str(input("¿Deseas conocer tu masa corporal? S (SI) / N (NO): "))
    if respuesta == "":
        print("No ingreso ningun dato, debe ingresar S (SI) / N (NO):") 
    elif respuesta.isdigit():
        print("No debe de ingresar números")
    elif respuesta.isalpha() == False: 
        print("Tipo de dato no reconocido") 
    elif respuesta == "N" : 
        print("Gracias por tu visita a NORMASCORP, nos vemos en otro momento. ")
        exit()
    elif respuesta == "n" : 
        print("Gracias por tu visita a NORMASCORP, nos vemos en otro momento. ")
        exit()
    else: 
        break
while True:
    nombre = str(input("Ingresa tu nombre, por favor: "))
    if nombre == "":
        print("No ingreso ningun dato, debe ingresar su nombre")
    elif nombre.isdigit():
        print("No debe de ingresar números")  
    elif nombre.isalpha() == False: 
        print("Tipo de dato no reconocido")
    else: 
        break
while True:
    apellidop=str(input("Ingresa tus apellido paterno, por favor: "))
    if apellidop == "":
        print("No ingreso ningun dato, debe ingresar su apellido")
    elif apellidop.isdigit():
        print("No debe de ingresar números")  
    elif apellidop.isalpha() == False: 
        print("Tipo de dato no reconocido")
    else :
            break
while True:
    apellidom=str(input("Ingresa tus apellido materno, por favor: "))
    if apellidom == "":
        print("No ingreso ningun dato, debe ingresar su apellido")
    elif apellidom.isdigit():
        print("No debe de ingresar números")  
    elif apellidom.isalpha() == False: 
        print("Tipo de dato no reconocido")
    else :
            break  
print("Mucho gusto en conocerte ", nombre + " " + apellidop + " " + apellidom )
print("Para poder dar tus resultados de masa corporal necesito que me proporciones mas datos para continuar")  
while True:
    try:
        edad=int(input("me puedes dar tu edad, por favor:  "))
    except ValueError:   
        print("Tipo de dato no reconocido, solo se permite número entero mayor a 1") 
        continue
    if edad <= 0:
         print("Tipo de dato no reconocido, solo se permite número entero mayor a 1") 
    else:
        break
while True:
    try:
        peso=float(input("me puedes dar tu peso, por favor:  " ))
    except ValueError:   
        print("Tipo de dato no reconocido, solo se permite número entero mayor a 1") 
        continue
    if peso <= 0:
         print("Tipo de dato no reconocido, solo se permite número entero mayor a 1") 
    else:
        break 
while True:
    try:
        estatura=float(input("me puedes dar tu estatura, por favor:  " ))
    except ValueError:   
        print("Tipo de dato no reconocido, solo se permite número entero mayor a 1") 
        continue
    if estatura <= 0:
         print("Tipo de dato no reconocido, solo se permite número entero mayor a 1") 
    else:
        break    
masacorporal= peso/estatura**2 
print("Hola ",nombre," tu edad es: ",edad, " tu peso es: ", peso, "tu estatura es: ", estatura, " tu masa corporal es: ", str(masacorporal))
if masacorporal >= 0 and masacorporal <= 15.99 :
    print ("Delgadez severa")
elif masacorporal >= 16.00 and masacorporal <= 16.99 : 
    print ("Delgadez moderada")
elif masacorporal >= 17.00 and masacorporal <= 18.49 :
    print ("Delgadez leve")
elif masacorporal >= 18.50 and masacorporal <= 24.99 :
    print ("Normal")
elif masacorporal >= 25.00 and masacorporal <= 29.99 :
    print ("Sobrepeso")
elif masacorporal >= 30.00 and masacorporal <= 34.99 :
    print ("obesidad leve")
elif masacorporal >= 35.00 and masacorporal <= 39.00 :
    print ("obesidad media")
elif masacorporal >= 40.00 :
    print ("obesidad morbida")
else: 
    masacorporal >= -1 
    print ("Fuera de rango, no se aceptan numeros negativos")    