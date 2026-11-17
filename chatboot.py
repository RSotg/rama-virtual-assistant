
# PROYECTO: RAMA - ASISTENTE VIRTUAL

import pandas as pd

# LEER LA BASE DE DATOS DE CLIENTES
clientes = pd.read_excel("clientes_sisit.xlsx", sheet_name="Clientes")

# LEER LA BASE DE DATOS DE FACTURA
facturas = pd.read_excel("clientes_sisit.xlsx", sheet_name="Facturas")

print("¡Base de datos conectada correctamente!")

# BUSCAR CLIENTE POR DNI

def buscar_cliente(dni):

    if not dni.isdigit():
        return None

    cliente = clientes[clientes["DNI"] == int(dni)]

    if not cliente.empty:
        return cliente.iloc[0]
    else:
        return None

    # BUSCAR FACTURAS POR ID DE CLIENTE

def buscar_facturas(id_cliente):

    resultado = facturas[facturas["Cliente"] == id_cliente]

    return resultado

# CONSULTAR DATOS DEL CLIENTE
def consultar_cliente():

    dni = input("\nPor favor, ingresa tu DNI: ")
    resultado = buscar_cliente(dni)

    if resultado is not None:
        print("\n¡Hola!", resultado["Nombre"])
        print("Tu plan es:", resultado["Plan"])
        print("Tu saldo es: $", resultado["Saldo"])

    else:
        print("\nNo encontramos un cliente con ese DNI.")

        input("\nPresiona Enter para volver al menú principal...")


# CONSULTAR FACTURACIÓN
def consultar_facturacion():

    dni = input("\nPor favor, ingresa tu DNI: ")
    resultado = buscar_cliente(dni)

    if resultado is not None:

        print("\n¡Claro! Te comparto el detalle de tus facturas:")

        mis_facturas = buscar_facturas(resultado["ID"])

        if not mis_facturas.empty:

            for _, factura in mis_facturas.iterrows():

                print("Período:", factura["Período"])
                print("Importe: $", factura["Importe"])
                print("Estado:", factura["Estado"])
                print("-------------------")

        else:
            print("No tienes facturas registradas.")

    else:
        print("\nNo encontramos un cliente con ese DNI.")

        


# PROBLEMAS CON MI INTERNET
def problemas_internet():

    while True:

        print("\n¡Vamos a revisar qué sucede con tu conexión!")
        print("\nSelecciona el problema que estás experimentando:\n")

        print("1. No tengo conexión a internet")
        print("2. Mi internet está lento")
        print("3. Mi router no enciende")
        print("4. Tengo cortes frecuentes")
        print("5. Ya intenté solucionarlo y sigo sin conexión")
        print("6. Volver al menú principal")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            print("\n¡Vamos a ayudarte! Primero revisaremos tu conexión.")
            print("Comprueba que tu router esté encendido y conectado.")

        elif opcion == "2":
            print("\nTe recomendamos reiniciar el router.")
            print("Espera unos segundos antes de volver a conectarlo.")

        elif opcion == "3":
            print("\nVerifica que el router esté conectado a la corriente.")
            print("Si no enciende, podría necesitar asistencia técnica.")

        elif opcion == "4":
            print("\nLamentamos los inconvenientes.")
            print("Vamos a revisar algunas posibles causas de los cortes.")

        elif opcion == "5":
            print("\nEntendemos. Vamos a derivarte con un asesor.")
            print("Estamos buscando un asesor disponible.")
            print("Hay varias personas esperando atención.")
            print("Aguarda un momentito, por favor.")

        elif opcion == "6":
            break

        else:
            print("\nNo reconocí esa opción. Intenta nuevamente.")
            continue

        input("\nPresiona Enter para continuar...")


# GESTIONES Y SOLICITUDES
def gestiones_solicitudes():

    while True:

        print("\n¡Claro! ¿Qué gestión necesitas realizar?\n")

        print("1. Cambiar mi plan de internet")
        print("2. Solicitar asistencia técnica")
        print("3. Consultar el estado de un reclamo")
        print("4. Solicitar la baja del servicio")
        print("5. Volver al menú principal")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            print("\n¡Con gusto! Podemos ayudarte a cambiar tu plan.")
            print("Un asesor podrá informarte sobre los planes disponibles.")

        elif opcion == "2":
            print("\nVamos a gestionar tu solicitud de asistencia técnica.")
            print("Un asesor podrá ayudarte con el inconveniente.")

        elif opcion == "3":
            print("\nPara consultar tu reclamo, necesitaremos tu número de reclamo.")
            numero = input("Ingresa tu número de reclamo: ")
            print("Estamos verificando el reclamo:", numero)
            print("Esta consulta será derivada a un asesor.")

        elif opcion == "4":
            print("\nLamentamos que estés considerando cancelar el servicio.")
            print("Un asesor podrá acompañarte con la solicitud de baja.")

        elif opcion == "5":
            break

        else:
            print("\nNo reconocí esa opción. Intenta nuevamente.")
            continue

        input("\nPresiona Enter para continuar...")



# FACTURACIÓN Y PAGOS
def menu_facturacion():

    while True:

        print("\n¡Claro! Estoy aquí para ayudarte con tu facturación.\n")

        print("1. Consultar mis facturas")
        print("2. Consultar mi saldo pendiente")
        print("3. Consultar fecha de vencimiento")
        print("4. Informar un pago realizado")
        print("5. Volver al menú principal")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            consultar_facturacion()

        elif opcion == "2":
            dni = input("\nIngresa tu DNI: ")
            resultado = buscar_cliente(dni)

            if resultado is not None:
                print("\nTu saldo pendiente es: $", resultado["Saldo"])
            else:
                print("\nNo encontramos un cliente con ese DNI.")

        elif opcion == "3":
            print("\nPara consultar tu fecha de vencimiento,")
            print("te recomendamos comunicarte con un asesor.")

        elif opcion == "4":
            print("\n¡Por supuesto! Vamos a registrar tu consulta.")
            print("Un asesor verificará el pago informado.")

        elif opcion == "5":
            break

        else:
            print("\nNo reconocí esa opción. Intenta nuevamente.")
            continue

        input("\nPresiona Enter para continuar...")





# MENÚ PRINCIPAL DE RAMA
def menu_principal():

    while True:

        print("\n¡Hola! Soy Rama, tu asistente virtual de SISIT Internet.")
        print("¿En qué puedo ayudarte hoy?\n")

        print("1. Mi cuenta")
        print("2. Facturación y pagos")
        print("3. Problemas con mi internet")
        print("4. Gestiones y solicitudes")
        print("5. Hablar con un asesor")
        print("0. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            consultar_cliente()

        elif opcion == "2":
            menu_facturacion()

        elif opcion == "3":
            problemas_internet()

        elif opcion == "4":
            gestiones_solicitudes()

        elif opcion == "5":
            print("\n¡Por supuesto! Estoy buscando un asesor disponible.")
            print("En este momento hay varias personas esperando atención.")
            print("Aguarda un momentito, por favor.")

            print("\nHorario de atención:")
            print("Lunes a viernes de 9:00 a 18:00 hs.")

            print("\nRecordá que también podés ingresar desde la app SISIT,")
            print("acceder a tu cuenta y cargar un reclamo.")
            print("Podrás consultar y seguir su gestión desde la misma app.")

        elif opcion == "0":
            print("\n¡Gracias por comunicarte con SISIT Internet!")
            print("¡Hasta pronto!")
            break

        else:
            print("\nNo reconocí esa opción. Por favor, intenta nuevamente.")


# INICIAR RAMA
menu_principal()








i