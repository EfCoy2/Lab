#definir clase
class Circulo():
    #constructor clase
    def __init__(self, radio):
        self.radio = radio
    #metodo para el perimetro
    def ObtenerPerimetro(self):
        perimetro = 2*self.radio*3.14159265358979323846
        return perimetro
    #metodo para el area
    def ObtenerArea(self):
        area = 3.14159265358979323846* self.radio**2
        return area
    #metodo para el volumen
    def ObtenerVolumen(self):
        volumen = (4/3)*3.14159265358979323846* self.radio**3
        return volumen
#valor radio
radio_circulo = 5.9812390813
#instancia de la clase
el_circulo = Circulo(radio_circulo)
perimetro = el_circulo.ObtenerPerimetro()
area = el_circulo.ObtenerArea()
volumen = el_circulo.ObtenerVolumen()

print(f"Perimetro de la circunferencia: {perimetro}")
print(f"Area de la circunferencia: {area}")
print(f"Volumen de la esfera: {volumen}")