import time

def read():
    suma1 = 0
    suma2 = 0
    suma3 = 0
    year = time.strftime("%Y")
    abrir = open('Datos.csv','r')
    lineas = abrir.read().splitlines()
    lineas.pop(0)
    for l in lineas:
        linea = l.split(';')
        fecha_usu = linea[2]
        cfn = fecha_usu.split("/")
        a_u = cfn[2]
        edad = (int(ano) - int(a_u))-1
        if edad >= 0 and edad < 18:
            suma1 = suma1 + 1
        if edad >= 18 and edad < 30:
            suma2 = suma2 + 1
        if edad >= 30:
            suma3 = suma3 + 1
        print linea[1]+" tiene "+str(edad)+" años"
    print "los usuarios menores a 18 años son: "+str(suma1)
    print "los usuarios  mayores a 18 y menores a 30 años son: "+str(suma2)
    print "los usaurios de usuarios mayores a 30 años son: "+str(suma3)

read()
