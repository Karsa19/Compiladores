from Practica1.automata.afn import AFN

class Conjuntos(object):

    afn= AFN()

    def __init__(self):
        pass

    Destados={}


    def recorrer_Destados(self, Destados):
        i=0

        for estado, conjunto in Destados.items():
            if '*' in estado:
                i+=1
        if i== len(Destados):
            return ''
        else:
            return 

    def marcar_estado(self, estado):
        pass


    def cerradura_Epsilon(self, conjunto_estados):
        cerradura=[]
        
        for e in conjunto_estados:
            cad='E'
            estado= e
            siguiente_estados = [estado, ]
            siguiente_indices = [0, ]
            afn.itera_af(siguiente_estados=siguiente_estados, cadena=cad, siguiente_indices=siguiente_indices)
            cerradura.append(siguiente_estados)

        list(dict.fromkeys(cerradura))

        return cerradura


    
    def mover(self, conjunto_estados, simbolo):
        mover=[]
        
        for e in conjunto_estados:
            cad=simbolo
            estado= e
            siguiente_estados = [estado, ]
            siguiente_indices = [0, ]
            afn.itera_af(siguiente_estados=siguiente_estados, cadena=cad, siguiente_indices=siguiente_indices)
            mover.append(siguiente_estados)

        list(dict.fromkeys(cerradura))

        return mover


    def hacer_Subconjuntos(self, afn):
        

        cerradura_A=cerradura_Epsilon(afn.obtener_incial)

        Destados['A']= cerradura_A


        while recorrer_Destados(Destados)==True: 
            marcar_estado()
            for a in afn.alfabeto: 
                U = cerradura_Epsilon(mover(T, a))
                if U not in Destados:
                    agregar U como estado sin marcar a Destados
                Dtran[T, a] = U
