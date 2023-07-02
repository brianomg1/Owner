import re
from datetime import datetime
def menu():
    print("PGY1121_015D")
    print("bienviendos jugadores")
    print("***"*20)
    print("----- MENÚ -----")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir Parejas")
    print("4. Salir")
    return validaNro(int , "opcion --> ",1,4)

def validaNro(tipo , texto, rMin=None ,rMax=None):
    while True:
        try:
            nro = tipo(input(texto))
            if rMin != None and rMax !=None :
                if rMin<=nro<=rMax:
                    break
                else:
                    print("fuega rango!!!")
            elif rMin != None:
                if rMin<=nro:
                     break
                else:
                    print(f"mín puede {rMin}")
            elif rMax != None:
                if nro<=rMax:
                    break
                else:
                    print(f"max puede {rMax}")
            else:
                break
        except:
            print("por favor responde respira!!")
    return nro

def validaLen(texto, largo, celular):
    while True:
        cell = input(texto)
        if celular:
            if len(cell)==largo:
                break
            else:
                print(f"falta numero hasta{largo}")
        else:
            if len(cell) >= largo:
                 break
            else:
                print(f"falta largo mínimo hasta {largo}")
    return cell

def validarnombre(self):
    if len(self.nombre) >= 2:
        return True
    else:
        return False

def validapajera(texto):
    while True:
        text = validaLen ("ingrese grupos jugar => ", True)
        if len(texto):
            grupo = False
            if text in texto:
                grupo = True
            if grupo:
                print("listo seguir grupo")
            else:
                break
        else:
            break
    return text


def validarcorreo():
    while True:
        correo=validaLen("Ingrese su email => ",6, False)
        if '@' in correo:
            if '.' in correo:
                break
            else:
                print("Falta el punto (.) dentro del correo")
        else:
            print("Falta el (@) dentro el correo.")
    return correo    
def validar_rut(ruts):
    continuar = True
    while continuar:
        ruts = ruts.replace(".", "").replace("-", "")
        if len(ruts) < 2:
            return False
        dv = ruts[-1].upper()
        ruts = ruts[:-1]
        if not dv.isdigit() and dv != 'K':
            return False
        suma = 0
        multiplicador = 2
        for digito in reversed(ruts):
            suma += int(digito) * multiplicador
            multiplicador += 1
            if multiplicador == 8:
                multiplicador = 2
        resto = suma % 11
        dv_esperado = str(11 - resto) if resto != 1 else 'K'
        if dv != dv_esperado:
            return False

    return True

def solicitar_categoria():
    while True:
        categoria = input("Ingrese la categoría del jugador (Oro, Plata o Bronce) (o 'q' para salir): ")
        if categoria.lower() == 'q':
            print("Saliendo del programa...")
            return None
        categorias_validas = ['oro', 'plata', 'bronce']
        if categoria.lower() not in categorias_validas:
                print("Categoría inválida. Las opciones válidas son: Oro, Plata o Bronce.")
        else:
            return categoria.capitalize()
        categoria_jugador = solicitar_categoria()
        if categoria_jugador is not None:
            print("Categoría registrada:", categoria_jugador)


def validaredad(fecha_nacimiento):
        fecha_actual = datetime.now().date()
        annos = fecha_actual.year - fecha_nacimiento.year
        if fecha_nacimiento.month > fecha_actual.month or (fecha_nacimiento.month == fecha_actual.month and fecha_nacimiento.day > fecha_actual.day):
            annos -= 1
        fecha_nacimiento = datetime(1940, 7, 10).date()
        annos = int(input())
        if annos != 18:
            print("La persona tiene menos de 80 años.")
        else:
            annos <= 80
            print("La persona tiene más de 80 años.")
def Grabar(nombres,
            ruts,
            nacias,
            categorias,
            fonos,
            grupos,
            annos,
            correos):
    nombres.append(input("ingrese nombre => "))
    ruts.append(validaNro(int,"Ingrese RUT => ", 5000000,99000000))
    fonos.append(validaLen("Ingrese su fono => ", 9, True))
    correos.append(validarcorreo())
    annos.append(validaredad(int,"ingrese edad => ",True))
    nacias.append(validaredad(int,"ingrese como => ",True))
    categorias.append("ingrese categoria",True )
    grupos.append(validapajera(input("ingrse grupo => ",2,True)))


def Buscar(ruts,nombres,categoria,fonos,correo):
    if len(nombres)!=0:
        opc=validaNro(int,"1.- Por rut\n2.-Por nombre\n3.-Por categoria \n4.- por fono \n5.- correo",1,5)
        print("su Lista de categoira es jugar")
        print("*"*20)
        if opc==1:
            ruts =validaNro(int("ingrese rut => ", 5000000,99000000))
            for j in range(len(nombres)):
                if ruts <= ruts[j]:
                    print(f"{ruts[j]} | {nombres[j]} | {categoria[j]} | {fonos[j]} | {correo[j]}")
        elif opc ==2:
            nombres = input("su nombre")
            for j in range(len(nombres)):
                if nombres <= nombres[j]:
                    print(f"{ruts[j]} | {nombres[j]} | {categoria[j]} | {fonos[j]} | {correo[j]}")
        elif opc ==3:
            categoria = print(f"su categoria{categoria}")
            if categoria <= categoria[j]:
                print(f"{ruts[j]} | {nombres[j]} | {categoria[j]} | {fonos[j]} | {correo[j]}")
        elif opc ==4:
            fonos =validaNro(int("ingrese fono => ", 9, True))
            for j in range(len(nombres)):
                if fonos <= fonos[j]:
                    print(f"{ruts[j]} | {nombres[j]} | {categoria[j]} | {fonos[j]} | {correo[j]}")
        elif opc ==5:
            correo = validarcorreo("ingrese correo => ", "@",True )
            for j in range(len(nombres)):
                if correo <= correo[j]:
                    print(f"{ruts[j]} | {nombres[j]} | {categoria[j]} | {fonos[j]} | {correo[j]}")

        else:
            print("no hay categoría!!")
    


def imprimir_parejas(identificador):
    parejas = [
    ("Jugador1", "EquipoA"),
    ("Jugador2", "EquipoB"),
    ("Jugador3", "EquipoA"),
    ("Jugador4", "EquipoC"),
    ("Jugador5", "EquipoB")
    ]
    parejas_encontradas = []
    for jugador, pareja in parejas:
        if pareja == identificador:
            parejas_encontradas.append(jugador)
    if parejas_encontradas:
        print("Integrantes del equipo", identificador + ":")
        for jugador in parejas_encontradas:
            print(jugador)
    else:
        print("No se encontraron parejas con el identificador", identificador)
        identificador_buscar = input("Ingrese el identificador de la pareja a buscar: ")
        imprimir_parejas(identificador_buscar)


def salir_programa():
        nombre_apellido = "Tu Nombre y Apellido"
        print("Saliendo del programa...")
        print("Gracias por utilizar el programa,", nombre_apellido)
        print("Opción inválida. Por favor, ingrese una opción válida.")