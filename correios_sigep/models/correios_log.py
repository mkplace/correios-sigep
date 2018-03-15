from collections import OrderedDict
from ..utils import dict as Dict
from ..utils.etree import parseDict
from lxml import etree
from ..models.plp import Plp
from ..models.sender import Sender
from ..models.postal_object import PostalObject

class CorreiosLog:
    def __init__(self, plp, sender_obj):
        
        if not isinstance(plp, Plp):
            raise Exception('parameter plp must have be an instance of Plp')

        if not isinstance(sender_obj, Sender):
            raise Exception('parameter sender_obj must have be an instance of Sender')

        self._correios_log = OrderedDict()
        self._correios_log['tipo_arquivo'] = 'Postagem',
        self._correios_log['versao_arquivo'] = 2.3,
        self._correios_log['plp'] = plp,
        self._correios_log['remetente'] = sender_obj,
        self._correios_log['objeto_postal'] = []

    @property
    def correios_log(self):
        return self._correios_log
    
    def addPostalObject(self, postal_object):
        if not isinstance(postal_object, PostalObject):
            raise Exception('postal_object must have be an instance of PostalObject')
            
        self._correios_log['objeto_postal'].append(postal_object)

    def getXml(self):
        xml_dict = Dict.toRecursiveDict(self._correios_log)
        correios_log = parseDict(xml_dict, 'correioslog')
        soap_package = etree.tostring(correios_log, encoding='ISO-8859-1')

        return soap_package.replace('\n', '')