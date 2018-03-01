from zeep import Client as ZeepClient


class Client(object):

    CORREIOS_WEBSERVICES = {
        'sigep-production': (
            'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',
            'AtendeCliente-production.wsdl',
        ),
        'sigep-test': (
            'https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',
            'AtendeCliente-test.wsdl',
        ),
        'websro': (
            'https://webservice.correios.com.br/service/rastro/Rastro.wsdl',
            'Rastro.wsdl',
        ),
        'freight': (
            'http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?WSDL',
            'CalcPrecoPrazo.asmx',
        ),
    }

    def __init__(self, username, password, environment='sigep-test'):
        self.username = username
        self.password = password
        self.WS = self.CORREIOS_WEBSERVICES[environment]

    def _request(self, method, *args, **kwargs):
        client = ZeepClient(self.WS[0])
        kwargs['usuario'] = self.username
        kwargs['senha'] = self.password

        fn = getattr(client, 'method')
        return fn()

    def verifica_disponibilidade_servico(self, *args, **kwargs):

        params = {
            'cod_administrativo': kwargs['codAdministrativo'],
            'numero_servico': kwargs['numeroServico'],
            'cep_origem': kwargs['cepOrigem'],
            'cep_destino': kwargs['cepDestino'],
            'usuario': kwargs['usuario'],
            'senha': kwargs['senha']
        }
        return self._request('verificaDisponibilidadeServico', **params)
