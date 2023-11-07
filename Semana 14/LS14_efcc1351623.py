class Automovil():
    def __init__(self):
        self.modelo=0
        self.precio=0.0
        self.marca=""
        self.disponible=True
        self.tipoCambioDolar=1.0
        self.descuentoAplicado=0.0
        
    def DefinirModelo(self, unModelo):
        self.modelo=unModelo
    def DefinirPrecio(self, unPrecio):
        self.precio=unPrecio
    def DefinirMarca(self, unaMarca):
        self.marca=unaMarca
    def DefinirtipoCambio(self, unTipoCambio):
        self.tipoCambioDolar=unTipoCambio
    def CambiarDisponibilidad(self):
        self.disponible=not self.disponible
    def MostrarDisponibilidad(self):
        if self.disponible:
            return "Disponible"
        else:
            return "No se encuentra disponible actualmente"
    def MostrarInformacion(self):
        precio_dolares=self.precio/self.tipoCambioDolar
        return f"Marca: {self.marca}. Modelo:  {self.modelo}. Precio:  Q{self.precio}. Precio en dolares:  ${precio_dolares}.  {self.MostrarDisponibilidad()}"
    def AplicarDescuento(self, miDescuento):
        self.descuentoAplicado=miDescuento
        self.precio -= miDescuento
        self.DefinirPrecio(self.precio)
auto = Automovil()
auto.DefinirModelo(2019)
auto.DefinirPrecio(189990.00)
auto.DefinirMarca("Mitsubishi")
auto.DefinirtipoCambio(7.82)
print(auto.MostrarInformacion())
auto.CambiarDisponibilidad()
print(auto.MostrarInformacion())
auto.AplicarDescuento(2500.15)
print(auto.MostrarInformacion())
auto.CambiarDisponibilidad()
print(auto.MostrarInformacion())
