class Pago:
    def __init__(self,fecha,monto,plataforma,comentario):
        self.fecha=fecha
        self.monto=monto
        self.plataforma=plataforma
        self.comentario=comentario

    def getFecha(self):
        return self.fecha
    def getMonto(self):
        return self.monto
    def getPlataforma(self):
        return self.plataforma
    def getComentario(self):
        return self.comentario
    
    def setFecha(self,fecha):
        self.fecha=fecha
    def setMonto(self,monto):
        self.monto=monto
    def setPlataforma(self,plataforma):
        self.plataforma=plataforma
    def setComentario(self,comentario):
        self.comentario=comentario            
