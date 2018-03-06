#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ..models.postal_object import PostalObject
from ..models.sender import Sender
from ..models.additional_service import AdditionalService
import qrcode
from elaphe import barcode
from hubarcode.datamatrix import DataMatrixEncoder
import re

class Tag:
    def __init__(self, sender, postal_object, id_postcard, group = ''):
        self.str_datamatrix = ''
        self.logo = ''
        if not isinstance(sender, Sender):
            raise Exception(
                'parameter sender is not valid. Must have be Sender instance')

        if not isinstance(postal_object, PostalObject):
            raise Exception(
                'parameter postal_object is not valid. Must have be PostalObject instance')

        self.generateDataMatrix(sender, postal_object, id_postcard)

    def mountStr(self, value):
        self.str_datamatrix += str (value)

    def generateDataMatrix(self, sender, postal_object, id_postcard):
        self.mountStr(postal_object.nacional.cep_destinatario)
        self.mountStr(postal_object.destinatario.numero_end_destinatario)
        self.mountStr(sender.cep_remetente)
        self.mountStr(sender.numero_remetente)
        self.mountStr(postal_object.nacional.cep_destinatario)
        self.mountStr('51')
        self.mountStr(postal_object.numero_etiqueta)
        self.mountStr(self.normalizeAdditionalServices(postal_object.servico_adicional))
        self.mountStr(id_postcard)
        self.mountStr(postal_object.codigo_servico_postagem)
        self.mountStr(postal_object.destinatario.numero_end_destinatario)
        self.mountStr(self.normalizeComplementAddress(postal_object.destinatario.complemento_destinatario))
        self.mountStr(self.normalizeDeclaredValue(postal_object.servico_adicional.valor_declarado))
        self.mountStr(self.normalizeTelephone(postal_object.destinatario.telefone_destinatario))
        self.mountStr('-00.000000')
        self.mountStr('-00.000000')
        self.mountStr('|')
        self.mountStr(''.ljust(30, ' '))
        
        encoder = barcode('datamatrix', self.str_datamatrix, options= dict(), margin=10)
        encoder.save("/tmp/test.png")

    @staticmethod
    def normalizeAdditionalServices(additional_service):
        return ''.join(additional_service.codigo_servico_adicional).ljust(12, '0')

    @staticmethod
    def normalizeComplementNumber(number):
        return str(number).ljust(4, '0')
    
    @staticmethod
    def normalizeDeclaredValue(value):
        return re.sub('[^0-9]+', '', str(value)).ljust(5, '0')

    @staticmethod
    def normalizeTelephone(number=''):
        return number.ljust(12, '0')
    
    @staticmethod
    def normalizeComplementAddress(complement):
        return complement.ljust(20, ' ')