class Clase:
    def __init__(self,grupo,fecha,pago,duracion,tipo,leccion,modulo):
        self.grupo = grupo
        self.fecha = fecha
        self.pago = pago
        self.duracion = duracion
        self.tipo = tipo
        self.leccion = leccion
        self.modulo = modulo

    #Declaramos Setters

    def setGrupo(self,grupo):
        self.grupo = grupo

    def setFecha(self,fecha):
        self.fecha = fecha

    def setPago(self,pago):
        self.pago = pago   

    def setDuracion(self,duracion):
        self.duracion = duracion     

    def setTipo(self,tipo):
        self.tipo = tipo    

    def setLeccion(self,leccion):
        self.leccion=leccion

    def setModulo(self,modulo):
        self.modulo=modulo       

    #Declaramos Getters
        
    def getGrupo(self):
        return self.grupo

    def getFecha(self):
        return self.fecha

    def getPago(self):
        return self.pago

    def getDuracion(self):
        return self.duracion
    
    def getTipo(self):
        return self.tipo
    
    def getLeccion(self):
        return self.leccion
    
    def getModulo(self):
        return self.modulo
    
