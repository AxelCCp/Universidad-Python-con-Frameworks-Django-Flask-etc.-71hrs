#ABC  = ABSTRACT BASE CLASS

from abc import ABC, abstractmethod


class FiguraGeoetrica(ABC):

    #EN LA CLASE 124 SE AGREGAN VALIDACIONES.   
    
    def __init__(self, ancho, alto) -> None:
         
        if self._validar_valor(ancho): 
            self._ancho = ancho
        else:
            self._ancho = 0 
            print(f'Valor erroneo - ancho: {ancho}')
    
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo - alto: {alto}')

        '''
        if 0 < ancho < 10: 
            self._ancho = ancho
        else:
            self._ancho = 0 
        if 0 < alto < 10:
            self._alto = alto
        else:
            self._alto = 0
        '''

    def __str__(self) -> str:
        return f'FiguraGeometrica: [alto: {self._alto}] [ancho: {self._ancho}]'
    

    #125 - validaciones - LLEVA UN GUION BAJO PARA ESTABLECER Q ESTE MÉTODO SOLO SE USARÁ DENTRO DE ESTA CLASE 
    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False
    
    #126
    @abstractmethod
    def calcularArea(self):
        pass
    
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if(self._validar_valor(ancho)):
            self._ancho = ancho
        else:
            print(f'Valor erroneo - ancho: {ancho}')
    
    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if(self._validar_valor(alto)):
            self._alto = alto
        else:
            print(f'Valor erroneo - alto: {alto}')
        