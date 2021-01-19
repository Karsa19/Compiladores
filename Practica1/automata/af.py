import os
from .estado import Estado
from .transicion import Transicion

class AF(object):
    def __init__(self, alfabeto=[], conj_estados={}, estado_inicial=0, conj_finales=[], es_afd=False):

        self.alfabeto= alfabeto
        self.conj_estados= conj_estados
        self.estado_inicial= estado_inicial
        self.conj_finales= conj_finales
        self._es_afd= True

    def cargar_desde(self, nombre):
        
        file= open(nombre)
        inicial = file.readline().split(':')
        final = file.readline().split(':')

        if len(inicial) == 2 and len(final) == 2:
            if inicial[0].strip() == 'inicial' and final[0].strip() == 'finales':
                self.establecer_inicial(inicial[1].strip())
                finales = [ f.strip() for f in final[1].split(',') ]
                finales = [ self.establecer_final(f) for f in finales ]
            else:
                print('El archivo debe tener los encabezados:  inicial, finales')
        else:
            print('El archivo debe tener un encabeza en este formato\n' + 
                    '    inicial:1\n' +
                    '    finales:11')
        for transicion in file:
            simbolo = transicion.split(',')
            estados = simbolo[0].split('->')
            simbolo = simbolo[1].strip()
            estados[0] = estados[0].strip()
            estados[1] = estados[1].strip()
            print('Estados = {estados}'.format(estados=estados))
            print('Simbolo = {simbolo}'.format(simbolo=simbolo))
            #transisiciones = [estados[0], estados[1], simbolo]
            self.agregar_estados(estados[0],  estados[1], simbolo, self.es_inicial(estados[0]), self.es_final(estados[0]))
            #self.agregar_estados(estados[1], self.es_inicial(estados[1]), self.es_final(estados[1]))
            self.agregar_transicion(estados[0], estados[1], simbolo)

    def _validar_int(self, i, err):
        try:
            return int(i)
        except ValueError:
            print(err)
            return -1

    def guardar_en(self, nombre):
        file= open("")

    def agregar_estados(self, etiqueta, destino, simbolo, inicial, final):
        try:
            self.conj_estados[etiqueta]
        except KeyError:
            self.conj_estados[etiqueta] = Estado(etiqueta=etiqueta, 
                    conj_trans=[Transicion(inicio=etiqueta, fin=destino, simbolo=simbolo),], 
                    inicial=inicial, final=final) 
    

    def agregar_transicion(self, inicio, fin, simbolo):
        for e in self.conj_estados:
            if self.conj_estados[e].etiqueta != inicio:
                self.conj_estados[e].agregar_transicion(inicio, fin, simbolo)
                
            elif self.conj_estados[e].etiqueta != fin:
                self.conj_estados[e].agregar_transicion(inicio, fin, simbolo)
                
            else:
                self.conj_estados[e].agregar_transicion(inicio, fin, simbolo)


    def eliminar_transicion(self, inicio, fin, simbolo):
        for e in self.conj_estados:
            if e.etiqueta == inicio:
                e.eliminar_transicion(inicio, fin, simbolo)
            
            elif e.etiqueta == fin:
                e.eliminar_transicion(inicio, fin, simbolo)



    def obtener_incial(self):
        return self.estado_inicial

    def obtener_finales(self):
        return self.conj_finales

    def establecer_inicial(self, estado):
        self.estado_inicial= estado


    def establecer_final(self, estado):
        self.conj_finales.append(estado)
    
    def es_final(self, estado):
        try:
            self.conj_finales.index(estado)
            return True
        except ValueError:
            return False
    
    def es_inicial(self, estado):
        return self.estado_inicial == estado

    def es_afn(self):
        for e in self.conj_estados:
            if self.conj_estados[e].estadoAFN() == True:
                self._es_afd= False
        
        if self._es_afd == False:
            return True
        else:
            return False
            

    def es_afd(self):

        for e in self.conj_estados:
            if e.estado_afn() == True:
                self._es_afd= False
        
        if self._es_afd == False:
            return False
        else:
            return True
    
    def acepta(self, cadena):
        cad= list(cadena)
        estado_actual=0


    def generar_cadena(self):
        pass

    