# 
# GitHub: @autor
#

# TODO

class Perro:
    def __init__(self):
        self.color = "Rojo"

    def CambiarColor(self, color):
        """Cambia el color"""
        if color != "violeta":
            self.color = color

Perro.CambiarColor("Violeta")


