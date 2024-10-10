opcion =0

while opcion !=6:
    print("MENU DE EJERCICIOS")
    print("1. Ejercicio 3.1")
    print("2. Ejercicio 3.2")
    print("3. Ejercicio 3.3")
    print("4. Ejercicio 3.4")
    print("5. Ejercicio 3.5")
    print("6. Salir")
    opcion = int (input("Ingrese una opcion: "))
    match opcion:
        case 1:
            num =1
            Inicio =1
            suma =0
            Elevado =0
            for Inicio in range (50):
                Elevado = num**3
                print (Elevado)
                suma = suma + Elevado
                num = num +1
            print ("La sumatoria es: ", suma)
        case 2:
            filas = int(input("Ingrese el número de filas: "))
            for i in range(1, filas + 1):
                print(" " * (filas - i), " ")
                print("* " * i)
        case 3:
            dimension =8
            fila =0
            Columna =0
            for fila in range(dimension):
                for Columna in range(dimension):
                    if (fila + Columna) %2==0:
                        print(" Bl ", end=" ")
                    else:
                        print(" Ne ", end=" ")
                print("")
        case 4:
            inicio = ""
            palabra = input("Ingrese una palabra: ")
            lista_letras = list(palabra)
            print("La palabra ", palabra, " invertida es: ")
            
            for inicio in reversed(palabra):
                print(inicio, end="")
            print("")
        case 5:
            Eleccion = 0

            while Eleccion != 3:
                Materiales = ["Lapiz", "Borrador", "Lapicero", "Cuaderno", "Libro", "Marcador", "Sacapuntas", "Corrector"]
                print("1. Mostrar lista")
                print("2. Buscar material")
                print("3. Salir")
                Eleccion = int(input("Ingrese una opción: "))

                match Eleccion:
                    case 1:
                        for material in Materiales:
                            print(material)
                
                    case 2:
                        Elemento = input("Ingrese el nombre del material a buscar: ").lower()
                        for material in Materiales:
                            if Elemento == material.lower():
                                print("Material Encontrado:", material)
                                break
                        else:
                                print("Material no encontrado")

                    case 3:
                        print("Finalizando programa...")