opcion =0
while opcion !=6:
    print("MENU DE EJERCICIOS")
    print("1. Ejercicio 1.1")
    print("2. Ejercicio 1.2")
    print("3. Ejercicio 1.3")
    print("4. Ejercicio 1.4")
    print("5. Ejercicio 1.5")
    print("6. Salir")
    print("------------------")
    opcion = int(input("Elija una opcion: "))

    match opcion:
        case 1:
            Letra = input("Digite una letra del abecedario: ").lower()
        
            if Letra.isalpha():
                if 'a' <= Letra <= 'm':
                    print("la letra ",Letra,"es de las primeras del abecedario")
                else:
                    print("la letra ",Letra,"es de las ultimas del abecedario")
            else:
                print("Letra invalida")
        case 2:
            Angulo = float(input("ingrese un angulo: "))
            if Angulo >= 0 and Angulo<=90:
                print("El angulo ingresado esta en el primer cuadrante")
            elif Angulo > 90 and Angulo <= 180:
             print("El angulo ingresado esta en el segundo cuadrante")
            elif Angulo >180 and Angulo <=270:
             print("El angulo ingresado esta en el tercer cuadrante")
            elif Angulo >270 and Angulo<=360:
                print("El angulo ingresado esta en el cuarto cuadrante")
            else:
                print("El angulo ingresado no esta en los 360 grados")
        case 3:
            Nota = float(input("ingrese su nota:"))
            if Nota >4.5:
                print("Rendimiento: Excelente")
            elif Nota >=3.5 and Nota < 4.5:
                print("Rendimiento: Bueno")
            elif Nota >= 3 and Nota <3.5:
                print("Rendimiento: Regular")
            elif Nota >= 0 and Nota <3:
                print("Rendimiento: Insuficiente")
            else:
                print("Nota invalida")
        case 4:
            temp = float(input("Introduce una temperatura (en grados Celsius): "))
            if temp <= 10:
                print("La temperatura es fría.")
            elif 10 < temp <= 25:
                print("La temperatura es templada.")
            else:
                print("La temperatura es cálida.")
        case 5 :
            palabra = str (input("ingrese la parabra 'Jengibre': "))
            if palabra == 'Jengibre':
                print("Si, ¡El Jengibre es la mejor planta de todos los tiempos!")
            elif palabra =="jengibre":
                print("No, ¡quiero un gran Jengibre!")
            else:
                print("Jengibre¡ No")
        case 6:
            print("Finalizando programa")
