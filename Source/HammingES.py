#Hamming 7-4 transformer, Made by Marco Rodríguez, Marcokistan 2025, CS project

command = ("")

print("----------------------------------------------------\nCorreción de Código de Hamming(7,4) - Calculadora Instantanea\nCreado por Marco Rodríguez, 1.0v\n----------------------------------------------------")

def askagain():
    global command
    command = ("")
    while command == (""):
        try:
            command = input("Especifica la Paridad: Par o Impar?: ")
        except:
            pass
    if command == ("Par"):
        paridadpar()
    elif command == ("Impar"):
        paridadimpar()
    else:
        askagain()

def paridadpar():
    bit1uno = False
    bit2uno = False
    bit3uno = False
    bit4uno = False
    bit5uno = False
    bit6uno = False
    bit7uno = False
    var1 = ("")
    var2 = ("")
    var3 = ("")
    var4 = ("")
    var5 = ("")
    var6 = ("")
    var7 = ("")
    int1 = 0
    int2 = 0
    int3 = 0
    int4 = 0
    int5 = 0
    int6 = 0
    int7 = 0
    sumatorioprimerbitparidad = 0
    sumatoriosegundobitparidad = 0
    sumatoriotercerobitparidad = 0
    insertedvar = input("Introduce un número binario de cuatro digitos: ")
    localcounter = len(insertedvar)
    if localcounter > 4 or localcounter < 4 or insertedvar.isdigit() == False or insertedvar[0] not in ('0', '1') or insertedvar[1] not in ('0', '1') or insertedvar[2] not in ('0', '1') or insertedvar[3] not in ('0', '1'):
        del bit1uno, bit2uno, bit3uno, bit4uno, bit5uno, bit6uno, bit7uno
        del insertedvar, localcounter, var1, var2, var3, var4, var5, var6, var7
        del int1, int2, int3, int4, int5, int6, int7
        paridadpar()
        return
    else:
        pass
    # bit one manages 1,3,5,7
    # bit two manages 2,3,6,7
    # bit three manages 4,5,6,7
    
    var7 = insertedvar[0]
    var6 = insertedvar[1]
    var5 = insertedvar[2]
    var3 = insertedvar[3]
    int7 = int(var7)
    int6 = int(var6)
    int5 = int(var5)
    int3 = int(var3)
    # first bit check
    sumatorioprimerbitparidad = int1 + int3 + int5 + int7
    if sumatorioprimerbitparidad % 2 != 0:
        int1 = 1
    else:
        int1 = 0
    # second bit check
    sumatoriosegundobitparidad = int2 + int3 + int6 + int7
    if sumatoriosegundobitparidad % 2 != 0:
        int2 = 1
    else:
        int2 = 0
    # third bit check
    sumatoriotercerobitparidad = int4 + int5 + int6 + int7
    if sumatoriotercerobitparidad % 2 != 0:
        int4 = 1
    else:
        int4 = 0

    var1 = str(int1)
    var2 = str(int2)
    var4 = str(int4)
    
    newhamming = (f"Hamming(7,4): {var7}{var6}{var5}{var4}{var3}{var2}{var1}\n\n")
    print(newhamming)
    del bit1uno, bit2uno, bit3uno, bit4uno, bit5uno, bit6uno, bit7uno
    del insertedvar, localcounter, var1, var2, var3, var4, var5, var6, var7
    del int1, int2, int3, int4, int5, int6, int7
    askagain()
    
def paridadimpar():
    global insertedvar
    bit1uno = False
    bit2uno = False
    bit3uno = False
    bit4uno = False
    bit5uno = False
    bit6uno = False
    bit7uno = False
    var1 = ("")
    var2 = ("")
    var3 = ("")
    var4 = ("")
    var5 = ("")
    var6 = ("")
    var7 = ("")
    int1 = 0
    int2 = 0
    int3 = 0
    int4 = 0
    int5 = 0
    int6 = 0
    int7 = 0
    sumatorioprimerbitparidad = 0
    sumatoriosegundobitparidad = 0
    sumatoriotercerobitparidad = 0
    insertedvar = input("Introduce un número binario de cuatro digitos: ")
    localcounter = len(insertedvar)
    if localcounter > 4 or localcounter < 4 or insertedvar.isdigit() == False or insertedvar[0] not in ('0', '1') or insertedvar[1] not in ('0', '1') or insertedvar[2] not in ('0', '1') or insertedvar[3] not in ('0', '1'):
        del bit1uno, bit2uno, bit3uno, bit4uno, bit5uno, bit6uno, bit7uno
        del insertedvar, localcounter, var1, var2, var3, var4, var5, var6, var7
        del int1, int2, int3, int4, int5, int6, int7
        paridadpar()
        return
    else:
        pass
    # bit one manages 1,3,5,7
    # bit two manages 2,3,6,7
    # bit three manages 4,5,6,7
    
    var7 = insertedvar[0]
    var6 = insertedvar[1]
    var5 = insertedvar[2]
    var3 = insertedvar[3]
    int7 = int(var7)
    int6 = int(var6)
    int5 = int(var5)
    int3 = int(var3)
    # first bit check
    sumatorioprimerbitparidad = int1 + int3 + int5 + int7
    if sumatorioprimerbitparidad % 2 == 0:
        int1 = 1
    else:
        int1 = 0
    # second bit check
    sumatoriosegundobitparidad = int2 + int3 + int6 + int7
    if sumatoriosegundobitparidad % 2 == 0:
        int2 = 1
    else:
        int2 = 0
    # third bit check
    sumatoriotercerobitparidad = int4 + int5 + int6 + int7
    if sumatoriotercerobitparidad % 2 == 0:
        int4 = 1
    else:
        int4 = 0

    var1 = str(int1)
    var2 = str(int2)
    var4 = str(int4)
    
    newhamming = (f"Hamming(7,4): {var7}{var6}{var5}{var4}{var3}{var2}{var1}\n\n")
    print(newhamming)
    del bit1uno, bit2uno, bit3uno, bit4uno, bit5uno, bit6uno, bit7uno
    del insertedvar, localcounter, var1, var2, var3, var4, var5, var6, var7
    del int1, int2, int3, int4, int5, int6, int7
    askagain()

askagain()


    
