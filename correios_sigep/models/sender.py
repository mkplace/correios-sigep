class Sender(object):
    def __init__(self, contract_number, director_number, administrative_code, sender_name,
                 address, number, complement, neighborhood, zipcode, city, state, telephone, fax, email):

        self.numero_contrato = contract_number
        self.numero_diretoria = director_number
        self.codigo_administrativo = administrative_code
        self.nome_remetente = sender_name
        self.logradouro_remetente = address
        self.numero_remetente = number
        self.complemento_remetente = complement
        self.bairro_remetente = neighborhood
        self.cep_remetente = zipcode
        self.cidade_remetente = city
        self.uf_remetente = state
        self.telefone_remetente = telephone
        self.fax_remetente = ''
        self.email_remetente = email