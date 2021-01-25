from collections import Counter
from .transicion import Transicion


class Estado(object):
    
    def __init__(self, etiqueta=0, conj_trans=[], inicial=False, final=False):
        self.etiqueta= etiqueta
        self.conj_trans= conj_trans
        self.final= final
        self.inicial= inicial

    def __str__(self):
        estado = 'Estado ( etiqueta=' + self.etiqueta +\
            ', inicial=' + str(self.inicial) +\
            ', final=' + str(self.final) +\
            ', conj_trans=\n'
        
        for tran in self.conj_trans:
            estado += str(tran) + '\n'

        return estado

    
    def agregar_transicion(self, inicio, fin, simbolo):
        transicion= Transicion()
        transicion.inicio= inicio
        transicion.fin= fin
        transicion.simbolo= simbolo
        self.conj_trans.append(transicion)

    def eliminar_transicion(self, inicio, fin, simbolo):
        for t in self.conj_trans:
            if t.inicio == inicio & t.fin == fin & t.simbolo == simbolo:
                self.conj_trans.remove(t)


    def estado_afn(self):
        #for i, elem in enumerate(self.conj_trans):
        #    if counts_por_elem[elem] > 1:
        #        return True

        return False

