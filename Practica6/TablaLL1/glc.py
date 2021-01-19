import os
from .produccion import Produccion


class GLC(object):
    def __init__(self,variables=[], terminales=[], producciones=[], inicial=''):
        self.variables= variables
        self.terminales= terminales
        self.producciones= producciones
        self.inicial= inicial

    def cargar_desde(self, ruta):

        file= open(ruta)

        terminal= file.readline().split(':')

        if len(terminal)==2:
            if terminal[0].strip() == 'terminales':
                terminales = [ t.strip() for t in terminal[1].split(',') ]
                terminales = [ self.agregar_terminal(t) for t in terminales ]
            else:
                print('El archivo debe contener los terminales al inicio')

        produccion_1 = file.readline()
        p= produccion_1.split(' ')
        numero= p[0].strip()
        variable= p[1].strip()
        alfa= p[3].strip()

        self.definir_inicial(variable)
        self.agregar_variable(variable)
        self.agregar_produccion(numero, variable, alfa)

        for produccion in file:
            p= produccion.split(' ')
            numero= p[0].strip()
            variable= p[1].strip()
            alfa= p[3].strip()

            self.agregar_variable(variable)
            self.agregar_produccion(numero, variable, alfa)


    
    def _validar_int(self, i, err):
        try:
            return int(i)
        except ValueError:
            print(err)
            return -1

    def definir_inicial(self, inicial):
        self.inicial=inicial

    def agregar_variable(self, v):
        self.variables.append(v)

    def agregar_terminal(self, t):
        self.terminales.append(t)


    def agregar_produccion(self, numero, variable, alfa):  
        produccion= Produccion()
        produccion.numero= numero
        produccion.variable= variable
        produccion.alfa= alfa

        self.producciones.append(produccion)

    
    def obtener_terminales(self):
        return self.terminales


    def obtener_incial(self):
        return self.inicial
  


    