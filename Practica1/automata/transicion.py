
class Transicion(object):
    
    def __init__(self, inicio='0', fin='0', simbolo='E'):
        self.inicio= inicio
        self.fin= fin 
        self.simbolo= simbolo

    def __str__(self):
        return 'Transicion (inicio=' + self.inicio + ', fin=' + self.fin + ', simbolo=' + self.simbolo + ')'
