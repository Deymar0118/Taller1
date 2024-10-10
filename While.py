import random
opcion =0

while opcion !=6:
    print("MENU DE EJERCICIOS")
    print("1. Ejercicio 2.1")
    print("2. Ejercicio 2.2")
    print("3. Ejercicio 2.3")
    print("4. Ejercicio 2.4")
    print("5. Ejercicio 2.5")
    opcion = int(input("Elija una opcion: "))
    
    match opcion:
        case 1:
            num =20
            while num >=1:
                print (num)
                num = num -1
        case 2:
            num = 2
            while num <= 50:
                print (num)
                num = num+2
        case 3:
            Palabra = input("Digite una letra: ").lower()
            contador_vocales = 0
            inicio =0

            while inicio <  len(Palabra):
                if Palabra[inicio] == "a" or Palabra[inicio] == "e" or Palabra[inicio]== "i" or Palabra[inicio]=="o" or Palabra[inicio]== "u":
                    contador = contador +1
                inicio = inicio +1
            print(f"El número de vocales es:", contador)
                    
        case 4:
            Numero_Dado =0
            while Numero_Dado !=6:
                Numero_Dado = random.randint(1,6)
                print ("Numero ",Numero_Dado)
        case 5:
            
            Eleccion =0
            num = 0
            suma =0
            
            while Eleccion !=2:
                num = int(input("Ingrese un numero para la sumatoria: "))
                suma = suma + num
                print("Desea seguir sumando?")
                print("1. si")
                print("2. No")
                Eleccion = int (input("Elija una opcion: "))
            print("la suma total es: ", suma)
            