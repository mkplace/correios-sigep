# -*- coding: utf-8 -*-

from ..correios_sigep.client import Client
from ..correios_sigep.models import plp as TagPlp, sender
from ..correios_sigep.models import postal_object
from ..correios_sigep.models.recipient import Recipient
from ..correios_sigep.models.national import National
from ..correios_sigep.models.additional_service import AdditionalService
from ..correios_sigep.models.object_dimension import ObjectDimension
from ..correios_sigep.models.correios_log import CorreiosLog

from ..correios_sigep.utils.etree import parseDict
from ..correios_sigep.models.tag import Tag
from lxml import etree
from ..correios_sigep.reports.tag import Tag as ReportTag

# otbcomercial
# mkplace@102030
# def test_verifica_disponibilidade_servico():
#     params = {
#         'codAdministrativo': '17000190',
#         'numeroServico': '41068',
#         'cepOrigem': '04089001',
#         'cepDestino': '04313000'

#     }
#     client = Client('sigep', 'n5f9t8')
#     result = client.get_available_service(**params)
#     print result, 'aaaaaaaaaaaaaaaaaaa'
#     assert  1==2

# def test_busca_cliente():
#     params = {
#         'contract_id': '9912401862',
#         'id_postcard': '0072501197'
#     }

#     # 74558537000108
#     client = Client('16244974', '74558537', 'sigep-production')
#     result = client.get_card_services(**params)
    
#     # print result, 'AAAAAAAAAAAAA'
#     for field in result['contratos'][0]['cartoesPostagem'][0]['servicos']:
#         print field.codigo, field.descricao
    
#     assert(1==2)

# def test_get_range_tag():
#     params = {
#         'recipient_type': 'C',
#         'cnpj': '34028316000103',
#         'service': '40096',
#         'qtd': 10
#     }
#     # SZ27437914 BR,SZ27437914 BR
#     client = Client('sigep', 'n5f9t8')
#     result = client.get_range_tag(**params)
#     print result, 'RANGE TAG'
#     assert(1==2)

# def test_fecha_plp():
#     client = Client('sigep', 'n5f9t8')
    
#     tag = Tag('SZ27437914 BR')
#     tag.setDv('4')

#     plp = TagPlp.Plp('0067599079')

#     sender_obj = sender.Sender('9992157880', '72', '17000190', 'Bruno Casado',
#                   'Av. Leonardo da vinci', 146, 'Ap 31', 'Vl Guarani', 
#                   '04313000', 'Sao Paulo', 'SP', '11992590656', '', 'bagcnop@gmail.com')

#     recipient = Recipient('Wellington', '11992590656', '11992590656', 'wcesar@gmail.com', 'Rua samambaia', 438, 'AP 34')

#     # objetos de postagem
#     national = National(sender_obj.bairro_remetente, sender_obj.cidade_remetente, sender_obj.uf_remetente, sender_obj.cep_remetente)
#     servicos = []
#     servico_adicional = AdditionalService(0.00)
#     servico_adicional.addCode('001')
#     servicos.append(servico_adicional)

#     dimensao_objeto = ObjectDimension(ObjectDimension.ENVELOPE)
#     postalobject = postal_object.PostalObject(tag, '40215', '350', recipient, national, servicos,  dimensao_objeto)

#     objeto_postal = []
#     objeto_postal.append(postalobject)
    
#     xml_obj = CorreiosLog(plp, sender_obj)
#     xml_obj.addPostalObject(postalobject)
    
#     params = {
#         'id_plp': '12345',
#         'id_postcard': '0067599079',
#         'list_tags': [tag.clean(tag.tag)],
#         'xml': xml_obj.getXml()
#     }

#     result = client.close_pre_post_list(**params)
    
#     print result, 'RESULTADO'
#     assert(1 == 2)

# def test_get_range_tag():
#     params = {
#         'recipient_type': 'C',
#         'cnpj': '34028316000103',
#         'service': '40096',
#         'qtd': 10
#     }
#     # SZ27437914 BR,SZ27437914 BR
#     client = Client('sigep', 'n5f9t8')
#     result = client.get_range_tag(**params)
#     print result, 'RANGE TAG'
#     assert(1==2)

def test_make_tag():
    
    
    tag = Tag('SZ27437914 BR')
    tag.setDv('4')

    plp = TagPlp.Plp('0067599079')

    sender_obj = sender.Sender('9992157880', '72', '17000190', 'Bruno Casado',
                  'Av. Leonardo da vinci', 146, 'Ap 31', 'Vl Guarani', 
                  '04313000', 'Sao Paulo', 'SP', '11992590656', '', 'bagcnop@gmail.com')

    recipient = Recipient('Wellington', '11992590656', '11992590656', 'wcesar@gmail.com', 'Rua samambaia', 438, 'AP 34')

    # objetos de postagem
    national = National(sender_obj.bairro_remetente, sender_obj.cidade_remetente, sender_obj.uf_remetente, sender_obj.cep_remetente)
    servicos = []
    servico_adicional = AdditionalService(0.00)
    servico_adicional.addCode('001')
    servicos.append(servico_adicional)

    dimensao_objeto = ObjectDimension(ObjectDimension.ENVELOPE)
    postalobject = postal_object.PostalObject(tag, '40215', '350', recipient, national, servico_adicional,  dimensao_objeto)

    objeto_postal = []
    objeto_postal.append(postalobject)
    
    xml_obj = CorreiosLog(plp, sender_obj)
    xml_obj.addPostalObject(postalobject)
    
    params = {
        'id_plp': '12345',
        'id_postcard': '0067599079',
        'list_tags': [tag.clean(tag.tag)],
        'xml': xml_obj.getXml()
    }

    tag = ReportTag(sender_obj, postalobject, '0067599079')
    
    
    assert(1 == 2)
