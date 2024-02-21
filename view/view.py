#from model.clase import Clase

class view:
    def __init__(self):
        pass

    def menu(self):
        print("Sisema de Registro de clases Kodland.")
        print("1) Registrar nueva clase")
        print("2) Ver clases Registradas")
        print("3) Generar resumen del último mes")
        print("4) Salir")
        return input ("Seleccione una opción (1, 2, 3 o 4):\n-> ")


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
    
    def pedirLeccion(self):
        return input("Ingrese la lección dictada hoy: ")
    
    def pedirModulo(self):
        return input("Ingrese el módulo correspondiente a la leccion: ")
    
    def mostrarInfoClase(self,Clase):
        print ("\nA continuacion se detallan los datos cargados por el usuario a \n registrar en el archivo.")
        print (f"Clase: {Clase.getGrupo()}\nFecha:{Clase.getFecha()}\nPago:{Clase.getPago()}\nDuracion:{Clase.getDuracion()}\nLeccion:{Clase.getLeccion()}\nModulo:{Clase.getModulo()}")

    def pedirMes(self):
        return input("Ingrese el mes actual. Ej: 01,02,03\n")    

    def gananciaMes(self, actual, gananciaMensual):
        print(f"La ganancia mensual el mes {actual} es de: ${gananciaMensual} Dólares")

    def showClases(self,clase):
        print(f"Grupo: {clase.getGrupo()},\nFecha: {clase.getFecha()},\nPago: {clase.getPago()},\nDuracion: {clase.getDuracion()},\nLeccion: {clase.getLeccion()},\nModulo: {clase.getModulo()}")
        print(" ")