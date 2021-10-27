class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self,ncolor):
        if ncolor == "rojo":
            self.color = ncolor
        elif ncolor == "verde":
            self.color = ncolor
        elif ncolor == "amarillo":
            self.color = ncolor
        elif ncolor == "negro":
            self.color = ncolor
        elif ncolor == "blanco":
            self.color = ncolor


class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados += 1

    def cantidadAsientos(self):
        cantidad = 0
        for i in range(len(self.asientos)):
            if isinstance(self.asientos[i],Asiento):
                cantidad += 1
        return cantidad
    

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self,nregistro):
        self.registro = nregistro

    def asignarTipo(self, ntipo):
        if ntipo == "gasolina":
            self.tipo = ntipo
        elif ntipo == "electrico":
            self.tipo = ntipo

        
