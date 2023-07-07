#Esta seccion es una bienvenida
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
 #Aqui solicitamos el nombre, pero tiene validaciones, la primera es de espacio, la segunda por numeros y la tercera es caracteres especiales    
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
#Aqui de igual forma se pide el apellido y se realizan las mismas validaciones
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
#Aqui de igual forma se solicita el apellido materno y tambien cuenta con las validaciones
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
#Aqui se imprime una bienvenida con los datos que previamente el usuario ingreso , adicional se realiza el metodo capitalize para que se muestren las mayusculas decada palabra
print("\n \t Mucho gusto en conocerte ", nombre.capitalize() + " " + apellidop.capitalize() + " " + apellidom.capitalize() )
print("Para poder dar tus resultados de masa corporal necesito que me proporciones mas datos para continuar")
#Aqui iniciamos con la funcionalidad importante de programa, que es solicitar cada valor para realizar el calculo de masa
# las validaciones estan basadas con el tipo de dato que se ingresa para la edad se espera siempre un entero
# que no sea uno negativo.
# Para los de peso y estatura se busca un valos donde se apecten decimales, pero si es diferente no te deja avanzar  
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
        peso=float(input("me puedes dar tu peso, en kilos, por favor:  " ))
    except ValueError:   
        print("Tipo de dato no reconocido, solo se permite número entero mayor a 1") 
        continue
    if peso <= 0:
         print("Tipo de dato no reconocido, solo se permite número entero mayor a 1") 
    else:
        break 
while True:
    try:
        estatura=float(input("me puedes dar tu estatura, en metros, por favor:  " ))
    except ValueError:   
        print("Tipo de dato no reconocido, solo se permite número entero mayor a 1") 
        continue
    if estatura <= 0:
         print("Tipo de dato no reconocido, solo se permite número entero mayor a 1") 
    else:
        break    
#Aqui se realiza el calculo y las validaciones de los resultados, dependiendo al valor que se ingreso previamente
masacorporal= peso/estatura**2 
print("\n \t Hola ",nombre.capitalize(),"\n \t tu edad es: ",edad, "\n \t tu peso es: ", peso, "\n \t tu estatura es: ", estatura, "\n \t tu masa corporal es: ", str(masacorporal))
if masacorporal >= 0 and masacorporal <= 15.99 :
    print ("\t Delgadez severa")
elif masacorporal >= 16.00 and masacorporal <= 16.99 : 
    print ("\t Delgadez moderada")
elif masacorporal >= 17.00 and masacorporal <= 18.49 :
    print ("\t Delgadez leve")
elif masacorporal >= 18.50 and masacorporal <= 24.99 :
    print ("\t Normal")
elif masacorporal >= 25.00 and masacorporal <= 29.99 :
    print ("\t Sobrepeso")
elif masacorporal >= 30.00 and masacorporal <= 34.99 :
    print ("\t obesidad leve")
elif masacorporal >= 35.00 and masacorporal <= 39.00 :
    print ("\t obesidad media")
elif masacorporal >= 40.00 :
    print ("\t obesidad morbida")
else: 
    masacorporal >= -1 
    print ("Fuera de rango, no se aceptan numeros negativos")    