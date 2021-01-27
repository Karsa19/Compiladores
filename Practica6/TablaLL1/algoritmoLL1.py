from .glc import GLC
from .tablaM import TablaM

class AlgoritmoLL1(object):
    global tablaM: TablaM = TablaM()
    global glc: GLC = GLC()
    
    def __init__(self):
        pass
    
    def primero(self, alfa):

        primero=[]
        

        if alfa in glc.terminales:
            primero.append(alfa)
            return primero 
        
        if alfa[0] in glc.variables: 
            if p.variable== v:
                primero(p.alfa)

    

    def siguiente(self, variable):
        
        siguiente=[]

        if variable==glc.inicial:
            siguiente.append('$')
            return siguiente

        

