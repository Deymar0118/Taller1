opcion =0
while opcion !=6:
    print("MENU DE EJERCICIOS")
    print("1. Ejercicio 4.1")
    print("2. Ejercicio 4.2")
    print("4. Ejercicio 4.4")
    print("5. Ejercicio 4.5")
    print("6. Salir")
    opcion = int (input("Ingrese una opcion: "))
    match opcion:
        case 1:
            num1 = int(input("ingrese un numero: "))
            num2 = int (input("ingrese otro numero: "))
            
            sumar = lambda a , b : a + b
            print ("La suma de esos numero es igual a: ",sumar(num1,num2))
        case 2:
            num = int (input("ingrese un numero: "))
            
            Par = lambda a: a % 2
            if Par(num) ==0:
                print("el numero ",num, " es par")
            else:
                print("el numero ",num, " es impar")
        case 4:
            i =0
            lista = [1, 11, 45, 3, 76, 88, 786, 54, 2, 4, 7, 567, 765, 234, 65, 10, 9]
            print("listado de numeros")
            print (lista)
            
            Mayor = filter (lambda a: a >10, lista)
            
            print("listado de numeros mayores a 10")
            print (list(Mayor))
        case 5:
            i =0
            lista = [1, 11, 45, 3, 76, 88, 786, 54, 2, 4, 7, 567, 765, 234, 65, 10, 9]
            print("listado de numeros")
            print (lista)
            
            Cuadrado = map(lambda a: a **2,lista)
            print("listado de numeros elevados a la 2")
            print (list(Cuadrado))