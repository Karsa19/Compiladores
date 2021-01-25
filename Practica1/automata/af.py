import os
from .estado import Estado
from .transicion import Transicion

class AF(object):
    def __init__(self, alfabeto=[], conj_estados={}, estado_inicial=0, conj_finales=[], es_afd=False):
        self.acepta_estatus = False
        self.cadenas_generadas = []
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
            #print('Estados = {estados}'.format(estados=estados))
            #print('Simbolo = {simbolo}'.format(simbolo=simbolo))
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
        #file= open("")
        txt = ""
        inicial = "inicial:"
        finales = []
        for estado in self.conj_estados:
            if self.conj_estados[estado].final:
                finales.append(estado)
            if self.conj_estados[estado].inicial:
                inicial = inicial + str(estado)
            for transicion in self.conj_estados[estado].conj_trans:
                txt = txt + transicion.inicio + "->" + transicion.fin + "," + transicion.simbolo + "\n"

        print(inicial)
        print("finales:" + ",".join(finales))
        print(txt)


    def agregar_estados(self, etiqueta, destino, simbolo, inicial, final):
        try:
            self.conj_estados[etiqueta]
        except KeyError:
            self.conj_estados[etiqueta] = Estado(etiqueta=etiqueta,
                    conj_trans=[],
                    inicial=inicial, final=final) 
    

    def agregar_transicion(self, inicio, fin, simbolo):
        for e in self.conj_estados:
            if str(inicio) == str(e):
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
        return self.conj_estados[self.estado_inicial]

    def obtener_finales(self):
        return self.conj_finales

    def establecer_inicial(self, estado):
        self.estado_inicial= estado


    def establecer_final(self, estado):
        self.conj_finales.append(estado)
        self.conj_estados[estado] = Estado(etiqueta=estado,
                                             conj_trans=[],
                                             inicial=False, final=True)

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
        self.acepta_estatus = False
        cad= list(cadena)
        estado_inicial: Estado = self.obtener_incial()
        siguiente_estados = [estado_inicial, ]
        siguiente_indices = [0, ]
        self.itera_af(siguiente_estados=siguiente_estados, cadena=cad, siguiente_indices=siguiente_indices)
        return self.acepta_estatus

    def itera_af(self, siguiente_estados=[], cadena=[], siguiente_indices=[]):
        contador = 0
        for estado in siguiente_estados:
            indice = siguiente_indices[contador]
            sig_edos, sig_indice = self.obten_sig_edo(estado, cadena, indice)
            if len(sig_edos) > 0:
                self.itera_af(sig_edos, cadena, sig_indice)
            contador += 1

    def obten_sig_edo(self, estado: Estado, cadena=[], indice=0):
        siguiente_estados = []
        siguiente_indices = []
        if indice < len(cadena):
            token = cadena[indice]
            for t in estado.conj_trans:
                if t.simbolo == token:
                    #print(str(estado.etiqueta) + " => " + token + ", " + str(self.conj_estados[t.fin]))
                    siguiente_estados.append(self.conj_estados[t.fin])
                    siguiente_indices.append(indice+1)
                elif t.simbolo == "E":
                    #print(str(estado.etiqueta) + " => E, " + str(self.conj_estados[t.fin]))
                    siguiente_estados.append(self.conj_estados[t.fin])
                    siguiente_indices.append(indice)
                if self.es_final(t.fin) and indice == len(cadena)-1:
                    self.acepta_estatus = True

        return siguiente_estados, siguiente_indices

    def generar_cadena(self, longitud):
        cad = ["" for i in range(longitud)]
        estado_inicial: Estado = self.obtener_incial()
        siguiente_estados = [estado_inicial, ]
        siguiente_indices = [0, ]
        siguiente_cadena = [cad, ]
        self.itera_af_(siguiente_estados=siguiente_estados, siguiente_cadenas=siguiente_cadena, siguiente_indices=siguiente_indices)
        return cad


    def itera_af_(self, siguiente_estados=[], siguiente_cadenas=[], siguiente_indices=[]):
        contador = 0
        for estado in siguiente_estados:
            indice = siguiente_indices[contador]
            cadena = siguiente_cadenas[contador]
            sig_edos, sig_indice, sig_cadena = self.obten_sig_edo_(estado, cadena, indice)
            #print("------------------------------")
            #print(sig_cadena)
            if len(sig_edos) > 0:
                self.itera_af_(sig_edos, sig_cadena, sig_indice)
            contador += 1

    def obten_sig_edo_(self, estado: Estado, cadena=[], indice=0):
        siguiente_estados = []
        siguiente_indices = []
        siguiente_cadenas = []
        if indice < len(cadena):
            # token = cadena[indice]
            for t in estado.conj_trans:
                cad = cadena[:]
                if t.simbolo != "E":
                    #print(str(t))
                    cad[indice] = t.simbolo
                    #print("cad[" + str(indice) + "] = " + t.simbolo)
                    siguiente_estados.append(self.conj_estados[t.fin])
                    siguiente_indices.append(indice+1)
                    siguiente_cadenas.append(cad)
                elif t.simbolo == "E":
                    siguiente_estados.append(self.conj_estados[t.fin])
                    siguiente_indices.append(indice)
                    siguiente_cadenas.append(cad)

                if self.es_final(t.fin):
                    self.cadenas_generadas.append(''.join(cad))

        return siguiente_estados, siguiente_indices, siguiente_cadenas
