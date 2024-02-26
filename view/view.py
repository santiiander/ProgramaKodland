#from model.clase import Clase
#Dato
class view:
    def __init__(self):
        pass

    def menu(self, nombre):
        print(f"Sistema de registro de clases Kodland. 👨‍💻\nBienvenido {nombre}")
        print("1) Registrar nueva clase 👩‍🏫")
        print("2) Ver clases registradas 📚")
        print("3) Generar resumen de cierto mes 🗓️")
        print("4) Generar constancia de cobro 💰")
        print("5) Eliminar clase del registro 🗑️")
        print("6) Registrar pago recibio 💸")
        print("7) Salir 🚪")
        return input("Seleccione una opción (1, 2, 3, 4, 5, 6 o 7):\n-> ")


    def FileNotFound(self):
        print("El archivo TXT contenedora de las clases \n no exixte") 

    def pedirGrupo(self):
        return input("Ingrese el grupo a registrar: ") 

    def pedirFecha(self):
        return input("Ingrese la fecha de la clase a registrar: ")

    def pedirPago(self):
        return input("Ingrese el pago de la clase: ")

    def pedirDuracion(self):
        return input("Ingrese la duracion de la clase en minutos: ") 
    
    def pedirTipo(self):
        return input("Ingrese el tipo de clase: ")
    
    def pedirLeccion(self):
        return input("Ingrese la lección dictada hoy: ")
    
    def pedirModulo(self):
        return input("Ingrese el módulo correspondiente a la leccion: ")
    
    def mostrarInfoClase(self,Clase):
        print ("\nA continuacion se detallan los datos cargados por el usuario a \nregistrar en el archivo.")
        print (f"Clase: {Clase.getGrupo()}\nFecha:{Clase.getFecha()}\nPago:${Clase.getPago()}USD\nDuracion:{Clase.getDuracion()}\nTipo: {Clase.getTipo()}\nLeccion:{Clase.getLeccion()}\nModulo:{Clase.getModulo()}\n")

    def pedirMes(self):
        return input("Ingrese el mes en formato numérico. Ej: 02 03 11\n")

    def gananciaMes(self, actual, gananciaMensual):
        print(f"La ganancia mensual el mes {actual} es de: ${gananciaMensual} Dólares")

    def showClases(self,clase):
        print(f"Grupo: {clase.getGrupo()}\nFecha: {clase.getFecha()}\nPago: ${clase.getPago()}\nDuracion: {clase.getDuracion()}\nTipo: {clase.getTipo()}\nLeccion: {clase.getLeccion()}\nModulo: {clase.getModulo()}")
        print(" ")

    def pedirNombre(self):
        return input(f"Ingrese su nombre para generar el resumen del uso del Software:\n")
    
    def generado(self):
        print("Resumen generado con exito y guardado de forma local.")

    def eliminarFecha(self):
        return input("Ingrese la fecha de la clase que quiere eliminar en formato dd/mm/aaaa: ")
    
    def eliminarGrupo(self):
        return input("Ingrese el código del grupo de la clase que quiere eliminar: ")
    
    def eliminada(self):
        print("Clase eliminada exitosamente si existia.\n")


    # Prints del modelo Pago

    def fechaPago(self):
        return input("Ingrese la fecha del efecto de pago dd/mm/aaaa: ")

    def montoPago(self):
        return input("Ingrese el monto cobrado: ")    
    
    def plataformaPago(self):
        return input("Ingrese la plataforma en la cual fue acreditada el pago: ")
    
    def comentarioPago(self):
        return input("Puede ingresar un comentario sobre la experiencia de cobro: ")