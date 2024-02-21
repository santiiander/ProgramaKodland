from model.clase import Clase
from view.view import view

class Controlador:
    def __init__(self):
        self.view = view()
        self.Clase=Clase(grupo="",fecha="",pago="",duracion="",leccion="",modulo="")
        self.listaClases=[]
        self.listaResumenMes=[]
        self.listaClasesNuevas = []
        self.gananciaMensual = 0


    def cargarListaClases(self):
        try:
            with open("clases.txt","r",encoding="UTF-8") as file:
                for lineas in file.readlines():
                    linea = lineas.strip().split(",")
                    self.Clase=Clase(linea[0],linea[1],linea[2],linea[3],linea[4],linea[5])
                    self.listaClases.append(self.Clase)
        except FileNotFoundError:
            self.view.FileNotFound()  

    def resumenMes(self):
        actual = self.view.pedirMes()
        for clase in self.listaClases:
            mes = clase.getFecha()
            pago = clase.getPago()
            fecha = mes.strip().split("-")
            mesfinal = fecha[1]
            if mesfinal == actual:
                self.gananciaMensual = 0
                self.gananciaMensual += float(pago)
        self.view.gananciaMes(actual, self.gananciaMensual)


    def mostrarClases(self):
        for clase in self.listaClases:
            self.view.showClases(clase)

    def cargarClase(self):

        grupo = self.view.pedirGrupo()
        fecha = self.view.pedirFecha()
        pago = self.view.pedirPago()
        duracion = self.view.pedirDuracion()
        leccion = self.view.pedirLeccion()
        modulo = self.view.pedirModulo()

        clase = Clase(grupo, fecha, pago, duracion, leccion, modulo)
        self.Clase.setGrupo(grupo)
        self.Clase.setFecha(fecha)
        self.Clase.setPago(pago)
        self.Clase.setDuracion(duracion)
        self.Clase.setLeccion(leccion)
        self.Clase.setModulo(modulo)
        self.listaClasesNuevas.append(clase)

    def subirDatos(self):
        #import datetime
        with open("clases.txt", "a+") as file:
            for clase in self.listaClasesNuevas:
                file.write(str(clase.getGrupo()) + "," + str(clase.getFecha()) + "," + str(clase.getPago()) + "," + str(clase.getDuracion()) + "," + str(clase.getLeccion()) + "," + str(clase.getModulo()) + "\n")
                #file.write("Clase: "+str(clase.getGrupo()) + "," +"Fecha: "+ str(clase.getFecha()) + "," +"Pago: "+ str(clase.getPago()) + "," +"Duracion: "+ str(clase.getDuracion()) + "\n")
        self.view.mostrarInfoClase(clase)
                
    def ejecutarSistema(self):
        while True:
            chose = self.view.menu()
            self.gananciaMensual = 0
            if chose == "1":
                self.cargarClase()
                self.subirDatos()
            if chose == "2":
                self.cargarListaClases()
                self.mostrarClases()
            if chose == "3":
                self.gananciaMensual = 0
                self.cargarListaClases()
                self.resumenMes()
            if chose == "4":
                break    


                    