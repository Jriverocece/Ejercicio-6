from FechaHora import FechaHora


def bisiesto(a):
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        return True
    else:
        return False


def valida(d, mes, a, h, m, s):
    if (a in range(3000)):
        if (mes in range(13)):
            if (mes == 11 or mes == 4 or mes == 6 or mes == 9):
                if (d in range(30)):
                    if (h in range(24)):
                        if (m in range(60)):
                            if (s in range(60)):
                                return True
                            else:
                                print("Los valores válidos son de 0..59")
                                return False
                        else:
                            print("Los valores válidos son de 0..59")
                            return False
                    else:
                        print("Los valores válidos son de 1..23")
                        return False
                else:
                    print("Los valores válidos para dias en el mes ", mes, " son de 1..30")
                    return False
            else:
                if (
                        mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 10 or mes == 12):
                    if (d in range(31)):
                        if (h in range(24)):
                            if (m in range(60)):
                                if (s in range(60)):
                                    return True
                                else:
                                    print("Los valores válidos son de 0..59")
                                    return False
                            else:
                                print("Los valores válidos son de 0..59")
                                return False
                        else:
                            print("Los valores válidos son de 1..23")
                            return False
                    else:
                        print("Los valores válidos para dias en el mes ", mes, " son de 1..31")
                        return False
                else:
                    if (mes == 2 and bisiesto(a)):
                        if (d in range(1, 30)):
                            if (h in range(24)):
                                if (m in range(60)):
                                    if (s in range(60)):
                                        return True
                                    else:
                                        print("Los valores válidos son de 0..59")
                                        return False
                                else:
                                    print("Los valores válidos son de 0..59")
                                    return False
                            else:
                                print("Los valores válidos son de 1..23")
                                return False
                        else:
                            print("Los valores válidos para dias en el mes ", mes, " son de 1..29")
                            return False
                    else:
                        if (d in range(1, 29)):
                            if (h in range(24)):
                                if (m in range(60)):
                                    if (s in range(60)):
                                        return True
                                    else:
                                        print("Los valores válidos son de 0..59")
                                        return False
                                else:
                                    print("Los valores válidos son de 0..59")
                                    return False
                            else:
                                print("Los valores válidos son de 1..23")
                                return False
                        else:
                            print("Los valores válidos para dias en el mes ", mes, " son de 1..28")
                            return False

def zero():
    print("\n\t\t\t --------- FIN DEL PROGRAMA ---------")

def one(UnaFecha,OtraFecha):
    print("\t\t\tSUMA")
    print("Hora 1: ",UnaFecha.getHORA()," + ", "Hora 2: ",OtraFecha.getHORA())
    suma= UnaFecha + OtraFecha
    print ('Hora RESULTANTE:\n   ',suma)

def two(UnaFecha,OtraFecha):
    print("\t\t\tRESTA")
    print("Hora 1: ",UnaFecha.getHORA()," - ", "Hora 2: ",OtraFecha.getHORA())
    resta= UnaFecha - OtraFecha
    print("HORA RESULTANTE:\n ", resta)

def three(UnaFecha,OtraFecha):
    print("\t\t\tMAYOR")
    print("Hora 1: ", UnaFecha.getHORA(), " > ", "Hora 2: ", OtraFecha.getHORA())
    mayor = UnaFecha > OtraFecha
    print("HORA RESULTANTE:\n ", mayor)


switcher = {
    0: zero,
    1: one,
    2: two,
    3: three
 }

def switch(argument,UnaFecha,OtraFecha):
    func = switcher.get(argument, lambda x,y: print('\t\t\t\t\t\t\t>> Opción Incorrecta <<\n----------------------------------------------------------------------------------\n'))
    func(UnaFecha,OtraFecha)

if __name__ == '__main__':


    UnaFecha = FechaHora()
    UnaFecha.ponerEnHora(7, 17, 27)

    OtraFecha = FechaHora()
    OtraFecha.ponerEnHora(6, 12, 21)

    bandera = False  # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("")
        print('\t\t###############################')
        print("\t\t# 0- SALIR                    #")
        print("\t\t# 1- SUMAR HORA               #")
        print("\t\t# 2- RESTAR HORA              #")
        print('\t\t# 3- MAYOR ENTRE DOS HORAS    #')
        print('\t\t###############################')
        opcion= int(input("\n\t\t>>Ingrese una opción:  "))
        print('\n----------------------------------------------------------------------------------')
        switch(opcion,UnaFecha,OtraFecha)
        bandera = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú