from .produccion import Produccion
from .glc import GLC

class TablaM(object):
    global glc: GLC = GLC()


    def __init__(self, num_fila=0, num_col=0):
        self.num_fila= num_fila
        self.num_col= num_col

    def crear_tabla(self):
        definir_num_col= len(glc.terminales)+2
        definir_num_fila= len(glc.variables)+1

        tabla=[num_col][num_fila]
        
    def llenar_tabla(self):
        pass  


    def definir_num_fila(fila):
        self.num_fila=fila
        
    def definir_num_col(col):
        self.num_col=col
    

    