import Opción_1 as op

nombre = []
ruts = []
nacia = []
categoria = []
fonos = []
grupo = []
annos = []
correo = []
opc=0
while opc != 9:
    opc=op.menu()
    if opc==1:
        nombre,ruts,nacia,categoria,fonos,grupo,annos,correo = op.Grabar(nombre,
        ruts,
        nacia,
        categoria,
        fonos,
        grupo,
        annos,
        correo)
    elif opc==2:
        ruts,nombre,categoria,fonos,correo = op.Buscar(ruts,nombre,categoria,fonos,correo)
    elif opc ==3:
        identificador = op.imprimir_parejas(identificador)
    elif opc ==4:
        nombre_apellido = op.salir_programa(nombre_apellido)
