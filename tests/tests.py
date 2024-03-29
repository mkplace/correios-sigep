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
from ..correios_sigep.reports.plp import Plp as ReportPlp

# otbcomercial
# mkplace@102030

def test_inicialization():
    client = Client('74558537000', '4wvp84', 'sigep-production')
    params = {
        'postcard_number': '0072501197'
    }
    
    print 'verifica postcard status: ' + client.get_postcard_status(**params)

    params = {
        'contract_id': '9912401862',
        'id_postcard': '0072501197'
    }
    result = client.get_card_services(**params)

    print 'verifica servicos disponiveis' 
    # print result
    for field in result['contratos'][0]['cartoesPostagem'][0]['servicos']:
        print field.codigo, field.descricao, field.id

    params = {
        'codAdministrativo': '16244974',
        'numeroServico': '04162                    ',
        'cepOrigem': '04089001',
        'cepDestino': '04313000'
    }

    result = client.get_available_service(**params)
    print 'servico disponivel:' + str(result)
    assert 1==2

# def test_postcard_status():
#     client = Client('74558537000', '4wvp84', 'sigep-production')
#     params = {
#         'postcard_number': '0072501197'
#     }
    
#     print client.get_postcard_status(**params)

#     assert 1==2

# def test_busca_cliente():
#     params = {
#         'contract_id': '9912401862',
#         'id_postcard': '0072501197'
#     }

#     # 74558537000108
#     client = Client('74558537000', '4wvp84', 'sigep-production')
#     result = client.get_card_services(**params)
    
#     # print result, 'AAAAAAAAAAAAA'
#     for field in result['contratos'][0]['cartoesPostagem'][0]['servicos']:
#         print field.codigo, field.descricao
    
#     assert(1==2)

# def test_verifica_disponibilidade_servico():
#     params = {
#         'codAdministrativo': '16244974',
#         'numeroServico': '04162',
#         'cepOrigem': '04089001',
#         'cepDestino': '04313000'
#     }

#     client = Client('74558537000', '4wvp84', 'sigep-production')
#     result = client.get_available_service(**params)
#     print result, 'aaaaaaaaaaaaaaaaaaa'
#     assert  1==2


def test_get_range_tag():
    params = {
        'recipient_type': 'C',
        'cnpj': '74558537000108',
        'service': '124849',
        'qtd': 2
    }
    # SZ27437914 BR,SZ27437914 BR
    client = Client('74558537000', '4wvp84', 'sigep-production')
    result = client.get_range_tag(**params)
    print result, 'RANGE TAG'
    assert(1==2)

# def test_fecha_plp():
#     client = Client('sigep', 'n5f9t8', 'sigep-production')
    
#     tag = Tag('SZ27437914 BR')
#     tag.setDv('4')

#     plp = TagPlp.Plp('0067599079')

#     sender_obj = sender.Sender('9992157880', '72', '17000190', 'Bruno Casado',
#                   'Av. Leonardo da vinci', 146, 'Ap 31', 'Vl Guarani', 
#                   '04313000', 'Sao Paulo', 'SP', '11992590656', '', 'bagcnop@gmail.com')
    
#     recipient = Recipient('Wellington', '11992590656', '11992590656', 'wcesar@gmail.com', 'Rua samambaia', 438, 'AP 34')

#     # objetos de postagem
#     national = National(sender_obj.bairro_remetente, sender_obj.cidade_remetente, sender_obj.uf_remetente, sender_obj.cep_remetente)
#     servico_adicional = AdditionalService(0.00)
#     servico_adicional.addCode('001')

#     dimensao_objeto = ObjectDimension(ObjectDimension.ENVELOPE)
#     postalobject = postal_object.PostalObject(tag, '40215', '350', recipient, national, servico_adicional,  dimensao_objeto)

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

#     print xml_obj.getXml()

#     result = client.close_pre_post_list(**params)
    
#     print result, 'RESULTADO'
#     assert(1 == 2)

# def test_get_range_tag2():
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

# def test_make_tag():
    
    
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
#     postalobject = postal_object.PostalObject(tag, '40215', '350', recipient, national, servico_adicional,  dimensao_objeto)

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
#     volume = { 'current_volume': 1, 'total_volume': 1, 'weight': 1000 }
#     tag = ReportTag(sender_obj, postalobject, '0067599079', '9912401862', volume)
#     file = open('/home/mkplace-dev001/teste.html', 'w')
#     # file.flush()
#     import unicodedata

#     u_html = tag.render(tag_type=ReportTag.TYPE_6P)
#     str_html = unicodedata.normalize('NFKD', u_html).encode('ascii', 'ignore')
#     tag.makePdf(str_html)

#     file.write(str(str_html))
#     file.close()
    
#     assert(1 == 2)

# def test_make_plp():
#     report = ReportPlp('12345', 1234567)
#     file = open('/home/mkplace-dev001/teste.html', 'w')
    
#     import unicodedata

#     u_html = report.render()
#     str_html = unicodedata.normalize('NFKD', u_html).encode('ascii', 'ignore')

#     file.write(str(str_html))
#     file.close()

#     report.makePdf(u_html)