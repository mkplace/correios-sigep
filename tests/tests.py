# -*- coding: utf-8 -*-

from ..correios_sigep.client import Client
from ..correios_sigep.models import plp as TagPlp, sender
from ..correios_sigep.models import postal_object
from ..correios_sigep.models.recipient import Recipient
from ..correios_sigep.models.national import National
from ..correios_sigep.models.additional_service import AdditionalService
from ..correios_sigep.models.object_dimension import ObjectDimension
from ..correios_sigep.utils import dict as Dict
from ..correios_sigep.utils.etree import parseDict
from lxml import etree


# def test_verifica_disponibilidade_servico():
#     params = {
#         'codAdministrativo': '17000190',
#         'numeroServico': '40215',
#         'cepOrigem': '11740000',
#         'cepDestino': '04313000'

#     }
#     client = Client('sigep', 'n5f9t8')
#     result = client.get_available_service(**params)
#     assert result


def test_busca_cliente():
    # params = {
    #     'contract_id': '9992157880',
    #     'id_postcard': '0067599079'
    # }

    # client = Client('sigep', 'n5f9t8')
    # result = client.get_card_services(**params)
    
    # print result, 'AAAAAAAAAAAAA'
    # for field in result['contratos'][0]['cartoesPostagem'][0]['servicos']:
    #     print field.codigo, field.descricao, 'aaaaaaaaaaaaaaaaaaaaaaaaa'
    
    assert(1==2)

# def test_get_range_tag():
#     params = {
#         'recipient_type': 'C',
#         'cnpj': '34028316000103',
#         'service': '04162',
#         'qtd': 2
#     }
#     # SZ27437914 BR,SZ27437914 BR
#     client = Client('sigep', 'n5f9t8')
#     result = client.get_range_tag(**params)


def test_fecha_plp():
    client = Client('sigep', 'n5f9t8')

    tags = ['SZ27437914 BR']
    tags_dv = ['4']

    tags_w_dv = []

    for index, tag in enumerate(tags):
        tags_w_dv.append(tag.replace(' ', tags_dv[index]))

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
    postalobject = postal_object.PostalObject(tags_w_dv[0], '04162', '350', recipient, national, servicos,  dimensao_objeto)

    objeto_postal = []

    objeto_postal.append(postalobject)
    
    from collections import OrderedDict
    xml_obj = OrderedDict()
    xml_obj['tipo_arquivo'] = 'Postagem',
    xml_obj['versao_arquivo'] = 2.3,
    xml_obj['plp'] = plp,
    xml_obj['remetente'] = sender_obj,
    xml_obj['objeto_postal'] = objeto_postal
    
    # print xml_obj

    xml_dict = Dict.toRecursiveDict(xml_obj)
    
    # print xml_dict, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    
    correios_log = parseDict(xml_dict, 'correioslog')
    
    # print Dict.toRecursiveDict(objeto_postal), 'AAAAAAAAAAAAAAAAA'
    # etree.tostring(parseDict(Dict.toRecursiveDict(objeto_postal), correios_log))
    soap_package = etree.tostring(correios_log, encoding='iso-8859-1')
    print soap_package.replace('\n', ''), 'xml'

    params = {
        'id_plp': '12345',
        'id_postcard': '0067599079',
        'list_tags': tags,
        'xml': "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?><correioslog><tipo_arquivo><![CDATA[Postagem]]></tipo_arquivo><versao_arquivo>2.3</versao_arquivo><plp><id_plp /><valor_global /><mcu_unidade_postagem /><nome_unidade_postagem /><cartao_postagem>0067599079</cartao_postagem></plp><remetente><numero_contrato>9992157880</numero_contrato><numero_diretoria>10</numero_diretoria><codigo_administrativo>17000190</codigo_administrativo><nome_remetente><![CDATA[EmpresaTeste]]></nome_remetente><logradouro_remetente><![CDATA[AvenidaCentral]]></logradouro_remetente><numero_remetente>2370</numero_remetente><complemento_remetente><![CDATA[Sala 1205,12°andar]]></complemento_remetente><bairro_remetente><![CDATA[Centro]]></bairro_remetente><cep_remetente>80002900</cep_remetente><cidade_remetente><![CDATA[Curitiba]]></cidade_remetente><uf_remetente>PR</uf_remetente><telefone_remetente><![CDATA[4130795008]]></telefone_remetente><fax_remetente><![CDATA[4191239321]]></fax_remetente><email_remetente><![CDATA[cli@mail.com.br]]></email_remetente></remetente><forma_pagamento /><objeto_postal><numero_etiqueta>SO000641962BR</numero_etiqueta><codigo_objeto_cliente /><codigo_servico_postagem>41068</codigo_servico_postagem><cubagem>0,00</cubagem><peso>2500</peso><rt1 /><rt2 /><destinatario><nome_destinatario><![CDATA[Cliente2]]></nome_destinatario><telefone_destinatario><![CDATA[6232339644]]></telefone_destinatario><celular_destinatario><![CDATA[62991239321]]></celular_destinatario><email_destinatario><![CDATA[cli2@mail.com.br]]></email_destinatario><logradouro_destinatario><![CDATA[Avenida Central2]]></logradouro_destinatario><complemento_destinatario><![CDATA[Qd: 102 ALt:04]]></complemento_destinatario><numero_end_destinatario>865</numero_end_destinatario></destinatario><nacional><bairro_destinatario><![CDATA[SetorIndustrial]]></bairro_destinatario><cidade_destinatario><![CDATA[Goiânia]]></cidade_destinatario><uf_destinatario>GO</uf_destinatario><cep_destinatario><![CDATA[74503100]]></cep_destinatario><codigo_usuario_postal /><centro_custo_cliente /><numero_nota_fiscal>112233</numero_nota_fiscal><serie_nota_fiscal /><valor_nota_fiscal /><natureza_nota_fiscal /><descricao_objeto /><valor_a_cobrar>0,0</valor_a_cobrar></nacional><servico_adicional><codigo_servico_adicional>025</codigo_servico_adicional><codigo_servico_adicional>001</codigo_servico_adicional><codigo_servico_adicional>019</codigo_servico_adicional><valor_declarado>3000,00</valor_declarado></servico_adicional><dimensao_objeto><tipo_objeto>002</tipo_objeto><dimensao_altura>50</dimensao_altura><dimensao_largura>30</dimensao_largura><dimensao_comprimento>60</dimensao_comprimento><dimensao_diametro>0</dimensao_diametro></dimensao_objeto><data_postagem_sara /><status_processamento>0</status_processamento><numero_comprovante_postagem /><valor_cobrado /></objeto_postal></correioslog>"
        
    }

    # 'xml': "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?><correioslog><tipo_arquivo>Postagem</tipo_arquivo><versao_arquivo>2.3</versao_arquivo><plp><id_plp /><valor_global/><mcu_unidade_postagem/><nome_unidade_postagem/><cartao_postagem>0067599079</cartao_postagem></plp><remetente><numero_contrato>9992157880</numero_contrato><numero_diretoria>10</numero_diretoria><codigo_administrativo>17000190</codigo_administrativo><nome_remetente><![CDATA[EmpresaTeste]]></nome_remetente><logradouro_remetente><![CDATA[AvenidaCentral]]></logradouro_remetente><numero_remetente>2370</numero_remetente><complemento_remetente><![CDATA[Sala 1205,12°andar]]></complemento_remetente><bairro_remetente><![CDATA[Centro]]></bairro_remetente><cep_remetente>80002900</cep_remetente><cidade_remetente><![CDATA[Curitiba]]></cidade_remetente><uf_remetente>PR</uf_remetente><telefone_remetente><![CDATA[4130795008]]></telefone_remetente><fax_remetente><![CDATA[4191239321]]></fax_remetente><email_remetente><![CDATA[cli@mail.com.br]]></email_remetente></remetente><forma_pagamento/><objeto_postal><numero_etiqueta>SO000641962BR</numero_etiqueta><codigo_objeto_cliente/><codigo_servico_postagem>41068</codigo_servico_postagem><cubagem>0,00</cubagem><peso>2500</peso><rt1/><rt2/><destinatario><nome_destinatario><![CDATA[Cliente2]]></nome_destinatario><telefone_destinatario><![CDATA[6232339644]]></telefone_destinatario><celular_destinatario><![CDATA[62991239321]]></celular_destinatario><email_destinatario><![CDATA[cli2@mail.com.br]]></email_destinatario><logradouro_destinatario><![CDATA[Avenida Central2]]></logradouro_destinatario><complemento_destinatario><![CDATA[Qd: 102 ALt:04]]></complemento_destinatario><numero_end_destinatario>865</numero_end_destinatario></destinatario><nacional><bairro_destinatario><![CDATA[SetorIndustrial]]></bairro_destinatario><cidade_destinatario><![CDATA[Goiânia]]></cidade_destinatario><uf_destinatario>GO</uf_destinatario><cep_destinatario><![CDATA[74503100]]></cep_destinatario><codigo_usuario_postal/><centro_custo_cliente/><numero_nota_fiscal>112233</numero_nota_fiscal><serie_nota_fiscal/><valor_nota_fiscal/><natureza_nota_fiscal/><descricao_objeto><![CDATA[]]></descricao_objeto><valor_a_cobrar>0,0</valor_a_cobrar></nacional><servico_adicional><codigo_servico_adicional>025</codigo_servico_adicional><codigo_servico_adicional>001</codigo_servico_adicional><codigo_servico_adicional>019</codigo_servico_adicional><valor_declarado>3000,00</valor_declarado></servico_adicional><dimensao_objeto><tipo_objeto>002</tipo_objeto><dimensao_altura>50</dimensao_altura><dimensao_largura>30</dimensao_largura><dimensao_comprimento>60</dimensao_comprimento><dimensao_diametro>0</dimensao_diametro></dimensao_objeto><data_postagem_sara/><status_processamento>0</status_processamento><numero_comprovante_postagem/><valor_cobrado/></objeto_postal><objeto_postal><numero_etiqueta>SL999221795BR</numero_etiqueta><codigo_objeto_cliente/><codigo_servico_postagem>40096</codigo_servico_postagem><cubagem>0,00</cubagem><peso>800</peso><rt1/><rt2/><destinatario><nome_destinatario><![CDATA[Cliente3]]></nome_destinatario><telefone_destinatario><![CDATA[6232339644]]></telefone_destinatario><celular_destinatario><![CDATA[62991239333]]></celular_destinatario><email_destinatario><![CDATA[cli3@mail.com.br]]></email_destinatario><logradouro_destinatario><![CDATA[AvenidaCentral3]]></logradouro_destinatario><complemento_destinatario><![CDATA[Qd: 102 A Lt:04]]></complemento_destinatario><numero_end_destinatario>285</numero_end_destinatario></destinatario><nacional><bairro_destinatario><![CDATA[Central]]></bairro_destinatario><cidade_destinatario><![CDATA[Goiânia]]></cidade_destinatario><uf_destinatario>GO</uf_destinatario><cep_destinatario><![CDATA[74503100]]></cep_destinatario><codigo_usuario_postal/><centro_custo_cliente/><numero_nota_fiscal>224455</numero_nota_fiscal><serie_nota_fiscal/><valor_nota_fiscal/><natureza_nota_fiscal/><descricao_objeto><![CDATA[]]></descricao_objeto><valor_a_cobrar>0,0</valor_a_cobrar></nacional><servico_adicional><codigo_servico_adicional>025</codigo_servico_adicional><codigo_servico_adicional>001</codigo_servico_adicional><codigo_servico_adicional>019</codigo_servico_adicional><valor_declarado>1000,00</valor_declarado></servico_adicional><dimensao_objeto><tipo_objeto>002</tipo_objeto><dimensao_altura>40</dimensao_altura><dimensao_largura>50</dimensao_largura><dimensao_comprimento>30</dimensao_comprimento><dimensao_diametro>0</dimensao_diametro></dimensao_objeto><data_postagem_sara/><status_processamento>0</status_processamento><numero_comprovante_postagem/><valor_cobrado/></objeto_postal></correioslog>"

    # print params, 'PARAMS'

    result = client.close_pre_post_list(**params)
    
    # print result, 'RESULTADO'
    assert(1 == 2)
