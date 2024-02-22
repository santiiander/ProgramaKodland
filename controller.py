from model.clase import Clase
from view.view import view

class Controlador:
    def __init__(self):
        self.view = view()
        self.Clase=Clase(grupo="",fecha="",pago="",duracion="",tipo="",leccion="",modulo="")
        self.listaClases=[]
        self.listaResumenMes=[]
        self.listaClasesNuevas = []
        self.gananciaMensual = 0
        self.nombreUsuario = ""
        self.espacios= " "*30
    
    def cargarListaClases(self):
        try:
            self.gananciaMensual = 0
            if not self.listaClases:  # Verifica si la lista está vacía
                with open("clases.txt", "r", encoding="UTF-8") as file:
                    for lineas in file.readlines():
                        linea = lineas.strip().split(",")
                        self.Clase = Clase(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5],linea[6])
                        self.listaClases.append(self.Clase)
        except FileNotFoundError:
            self.view.FileNotFound()

    def eliminarDelRegistro(self):
        fecha = self.view.eliminarFecha()
        grupo = self.view.eliminarGrupo()
        with open("clases.txt", "r") as file:
            lineas = file.readlines()

        with open("clases.txt", "w") as file:
            for linea in lineas:
                if fecha in linea and grupo in linea:
                    # Si la fecha y el grupo coinciden, no escribimos la línea de nuevo
                    continue
                file.write(linea)
        


    def resumenMes(self):
        actual = self.view.pedirMes()
        self.gananciaMensual = 0
        for clase in self.listaClases:
            mes = clase.getFecha()
            pago = clase.getPago()
            fecha = mes.strip().split("-")
            mesfinal = fecha[1]
            if mesfinal == actual:
                self.gananciaMensual += float(pago)    
        self.view.gananciaMes(actual, self.gananciaMensual)

    def reiniciar(self):
        self.gananciaMensual = 0


    def mostrarClases(self):
        for clase in self.listaClases:
            self.view.showClases(clase)

    def cargarClase(self):
        grupo = self.view.pedirGrupo()
        fecha = self.view.pedirFecha()
        pago = self.view.pedirPago()
        duracion = self.view.pedirDuracion()
        tipo = self.view.pedirTipo()
        leccion = self.view.pedirLeccion()
        modulo = self.view.pedirModulo()

        clase = Clase(grupo, fecha, pago, duracion, tipo, leccion, modulo)
        self.Clase.setGrupo(grupo)
        self.Clase.setFecha(fecha)
        self.Clase.setPago(pago)
        self.Clase.setDuracion(duracion)
        self.Clase.setTipo(tipo)
        self.Clase.setLeccion(leccion)
        self.Clase.setModulo(modulo)
        self.listaClasesNuevas.append(clase)

    def subirDatos(self):
        #import datetime
        with open("clases.txt", "a+") as file:
            for clase in self.listaClasesNuevas:
                file.write(str(clase.getGrupo()) + "," + str(clase.getFecha()) + "," + str(clase.getPago()) + "," + str(clase.getDuracion()) + "," + str(clase.getTipo())+ "," + str(clase.getLeccion()) + "," + str(clase.getModulo()) + "\n")
                #file.write("Clase: "+str(clase.getGrupo()) + "," +"Fecha: "+ str(clase.getFecha()) + "," +"Pago: "+ str(clase.getPago()) + "," +"Duracion: "+ str(clase.getDuracion()) + "\n")
        self.view.mostrarInfoClase(clase)

    def genResuemnArchivo(self):
        nombre = self.nombreUsuario
        fecha = self.view.pedirMes()
        try:
            with open(f"Resumen {nombre}, mes {fecha}.txt","a+") as file:
                file.write(f"{self.espacios}Resumen de {nombre}, correspondiente al mes {fecha}\n")
                for clase in self.listaClases:
                    mes = clase.getFecha()
                    fechaComparar = mes.strip().split("-")
                    mesfinal = fechaComparar[1] #Con esto obtenemos nuevamente el mes
                    if mesfinal==fecha:
                            #claseWrite = Clase(clase[0],clase[1],clase[2],clase[3],clase[4],clase[5])
                            file.write(" "*35+str(clase.getGrupo()) + "," + str(clase.getFecha()) + "," + str(clase.getPago()) + "," + str(clase.getDuracion()) + "," + str(clase.getTipo()) + "," + str(clase.getLeccion()) + "," + str(clase.getModulo()) + "\n")
        except FileNotFoundError:
                self.view.FileNotFound()
                     
    def ejecutarSistema(self):
        self.nombreUsuario = self.view.pedirNombre()
        while True:
            chose = self.view.menu(self.nombreUsuario)
            self.reiniciar()
            if chose == "1":
                self.reiniciar()
                self.cargarClase()
                self.subirDatos()
            elif chose == "2":
                self.reiniciar()
                self.cargarListaClases()
                self.mostrarClases()
            elif chose == "3":
                self.reiniciar()
                self.cargarListaClases()
                self.resumenMes()
            elif chose == "4":
                self.cargarListaClases()
                self.genResuemnArchivo()
                self.view.generado()
                pass
            elif chose == "5":
                self.cargarListaClases()
                self.eliminarDelRegistro()
                self.view.eliminada()
            elif chose == "6":
                break
