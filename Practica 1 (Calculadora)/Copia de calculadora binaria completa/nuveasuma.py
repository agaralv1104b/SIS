def main():    
    
    operando1:str = input("Ingrese el primer operando: ")
    operacion:str = input("+ / -: ")
    operando2:str = input("Ingrese el segundo operando: ")




    """este bloque es la validacion, para que:
        No acepte caracteres vacios
        Operando mayores que 8 bits
        Rellenar con 0 a la izquierda en caso necsario
        comprobar validez del signo incluyendo espacio en blanco
        """

    if operando1 == "" or operando2 == "":
        print("ERROR: los operando no pueden estar vacios...")
        exit()

    if len(operando1) > 8 or len(operando2) > 8:
        print("ERROR: los operando no pueden contener mas de 8 bits")
        exit() 

    if len(operando1) < 8 or len(operando2) < 8:

        #.zfill() hace que se rellene con 0 hata que sea 8 bits,
        #no hace falta meterla en una condicion pero me parecia mas claro asi
        # "si operando es menor que 8 rellenarlo"
        operando1 = operando1.zfill(8)
        operando2 = operando2.zfill(8)



    if operacion != "+" and operacion != "-" and operacion != "":
        print("ERROR: la operacion solo admite +/-")
        exit()




    lista1 = []
    lista2 = []

    for bit1 in operando1:

        """esta es la comprobacion para saber si estan introduciendo 0 y 1 solamente"""

        if bit1 != "1" and bit1 != "0":
            print("ERROR: solo se aceptaran 0 y 1")
            #este comando sirve para salir del programa cuando encuentre un fallo (no lo conocia)
            exit()

        else:
            #Parte los bits y los va añadiendo a la lista
            lista1.append(str(bit1))

    for bit2 in operando2:

        """Aqui igual que el anterior, la validacion apra que solo entren 1 y 0"""

        if bit2 != "1" and bit2 != "0":
            print("ERROR: solo se acpetaran 0 y 1")
            exit()

        else:
            #Parte los bits y los va añadiendo a la lista
            lista2.append(str(bit2))



    """Procesamiento de la operacion +"""

    resultado = ""
    acarreo = 0


    if operacion == "+" or operacion == "":
        for i in range(len(lista1) -1 , -1, -1):
            bit1 = int(lista1[i])
            bit2 = int(lista2[i])
            suma = bit1 + bit2 + acarreo

            if suma == 0:
                resultado = "0" + resultado
                acarreo = 0


            elif suma == 1:
                resultado = "1" + resultado 
                acarreo = 0

            elif suma == 2:
                resultado = "0" + resultado 
                acarreo = 1

            elif suma == 3:
                resultado = "1" + resultado 
                acarreo = 1

        if acarreo == 1: 
            resultado = "1" + resultado

        print(resultado)





    """Procesamineto de la operacion Resta"""

    resultado_negativo = ""
    acarreo_negativo = 0

    if operacion == "-" or operacion == "":

    #esta validacion fue confusa, si usamos int(operando1, 2), convierte el binario en decimal
    #una vez convertido se comprueba si es mayor que el operando1
    #esta pensado para que solo funcione cuando se introduce el signo "-"

        if int(operando2, 2) > int(operando1, 2):
            print("Resta negativa")
            exit()

        if operacion == "-" or operacion == "":

            for i in range (len(lista1) -1, -1, -1):
                bit1_negativo = int(lista1[i])
                bit2_negativo = int(lista2[i])
                resta = bit1_negativo - bit2_negativo - acarreo_negativo

                if resta == 0:
                    resultado_negativo = "0" + resultado_negativo
                    acarreo_negativo = 0

                elif resta == 1:
                    resultado_negativo = "1" + resultado_negativo
                    acarreo_negativo = 0

                elif resta == -1:
                    resultado_negativo = "1" + resultado_negativo
                    acarreo_negativo = 1

                elif resta == -2:
                    resultado_negativo = "0" + resultado_negativo
                    acarreo_negativo = 1

            print(resultado_negativo)

if __name__ == "__main__":
    main()

else:
    print("Modulo importado")
