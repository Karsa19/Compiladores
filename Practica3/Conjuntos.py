from Practica1.automata.afn import AFN

class Conjuntos(object):

    afn= AFN()

    def __init__(self):
        pass

    def hacer_Subconjuntos(self, afn):
        
        Destados={}

        cerradura_Epsilon(afn.obtener_incial)


        while ( hay un estado sin marcar T en Destados ): 
            marcar T
            for a in afn.alfabeto: 
                U = cerradura_Epsilon(mover(T, a))
                if U not in Destados:
                    agregar U como estado sin marcar a Destados
                Dtran[T, a] = U
 



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
