empleados = [
    # empleado 1
    {
        "nombre": "juan  carlos PEREZ ",
        "documento": "1.823.456.789",
        "correo": "jc.perez@empresa.com",
        "cargo": "analista",
        "ingreso": "15/03/2023"
    },

    # empleado 2
    {
        "nombre": "ANA maria Gomez",
        "documento": "52784",
        "correo": "ana.gomez@empresa",
        "cargo": "",
        "ingreso": "2022-11-01"
    },

    # empleado 3
    {
        "nombre": "Pedro Ramirez",
        "documento": "80a04512",
        "correo": "p.ramirez@empresa.co",
        "cargo": "desarrollador",
        "ingreso": "01/13/2024"
    },

    # empleado 4
    {
        "nombre": "maria  lopez",
        "documento": "12345",
        "correo": "maria@empresa.com",
        "cargo": "secretaria",
        "ingreso": "10/10/2023"
    },

    # empleado 5
    {
        "nombre": "Carlos Torres",
        "documento": "12345678",
        "correo":"carlostorres.empresa.com",
        "cargo": "analista",
        "ingreso": "2023-12-10"
    },

    # empleado 6
    {
        "nombre": "Laura Martinez",
        "documento": "123456789",
        "correo": "laura@empresa.co",
        "cargo": "",
        "ingreso": "31/12/2023"
    },

    # empleado 7
    {
        "nombre": " roberto  diaz ",
        "documento": "12345678",
        "correo": "roberto@empresa.com",
        "cargo": "vendedor",
        "ingreso": "32/01/2024"
    }
]

# Normalizamos el nombre: quitamos espacios y sobrantes
# y colocamos la primera letra de cada palabra en mayuscula.

def normalizar_nombre(nombre):
    nombre = " ".join(nombre.split()).title()
    return nombre

# Recorremos todos los empleados y corregimos su nombre.
for empleado in empleados:
    empleado["nombre"] = normalizar_nombre(empleado["nombre"])

# Limpiamos y validamos el numero de documento.
# El documento debe tener unicamente numeros entre 6 y 10 digitos.

def validar_documento(documento):
# Eliminamos puntos, guiones y espacios.
    documento = documento.replace(".","").replace("-","").replace(" ", "")

# Verificamos que el documento solamente tenga numeros
    if not documento.isdigit():
        return False, "El documento contiene letras"
    
# Verificamos que tenga entre 6 y 10 digitos.
    if len(documento) < 6 or len(documento) > 10:
        return False, "El documento debe tener entre 6 y 10 digitos"
    
# Si cumple todas las condiciones, el documento es valido.
    return True, ""

# Normalizamos el documento eliminando puntos, guiones y espacios.

def normalizar_documento(documento):
    return documento.replace(".", "") .replace("-", "") .replace(" ", "")

#validamos el correo electronico.

def validar_correo(correo):
    if correo.count("@") != 1:
        return False, "Debe tener exactamente un @"
    usuario, dominio = correo.split("@")

    if usuario == "":
        return False, "Debe tener caracteres antes del @"
    if not (correo.endswith(".com") or correo.endswith(".co")):
        return False, "Debe terminar en .com o .co"

    return True, ""

# Verificamos que el cargo del empleado no este vacio.

def validar_cargo(cargo):
    if cargo.strip() == "":
        return False, "El cargo esta vacio"

    return True, ""

# Validamos la fecha de ingreso y la convertimos en formato YYYY-MM-DD.

def validar_fecha(fecha):
    from datetime import datetime

    formatos = ["%d/%m/%Y", "%Y-%m-%d"]

    for formato in formatos:
        try:
            fecha_valida = datetime.strptime(fecha, formato)
            return True, fecha_valida.strftime("%Y-%m-%d") 
        except ValueError: pass

    return False, "La fecha no es valida"

# Procesamos un empleado y reunimos todos sus errores.

def procesar_empleado(empleado):
    errores = []

    valido, motivo = validar_documento(empleado["documento"])
    if not valido:
        errores.append(motivo)

    valido, motivo = validar_correo(empleado["correo"])
    if not valido:
        errores.append(motivo)

    valido, motivo = validar_cargo(empleado["cargo"])
    if not valido:
        errores.append(motivo)

    valido, motivo = validar_fecha(empleado["ingreso"])
    if not valido:
        errores.append(motivo)

    return errores

# Separamos los empleados validos de los rechazados.

validos = []
rechazados = []

for empleado in empleados:
    errores = procesar_empleado(empleado)

    if errores:
        rechazados.append({
            "empleado": empleado,
            "errores": errores
        })
    else: 
        empleado["documento"] = normalizar_documento(empleado["documento"])

        _, fecha_normalizada = validar_fecha(empleado["ingreso"])
        empleado["ingreso"] = fecha_normalizada

        validos.append(empleado)

# Mostramos los empleados validos.

print("\nEMPLEADOS VALIDOS:")
for empleado in validos:
    print(empleado)

# Mostramos los empleados rechazados.

print("\nEMPLEADOS RECHAZADOS:")
for rechazado in rechazados:
    print(rechazado["empleado"]["nombre"], ":", rechazado["errores"])

# Mostramos los totales finales

def mostrar_totales(empleados, validos, rechazados):
 print("\nRESUMEN:")
 print("Total procesados:", len(empleados))
 print("Total validos:", len(validos))
 print("Total rechazados:", len(rechazados))
mostrar_totales(empleados, validos, rechazados) 

# Contamos cuantas veces aparece cada motivo de rechazo.

frecuencia_errores = {}

for rechazado in rechazados:
    for error in rechazado["errores"]:
        if error in frecuencia_errores:
            frecuencia_errores[error] += 1
        else:
            frecuencia_errores[error] = 1

#Buscamos el error mas frecuente.

error_mas_frecuente = max(frecuencia_errores, key=frecuencia_errores.get)

print("Motivo de rechazo mas frecuente:", error_mas_frecuente)


    