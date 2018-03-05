from ..models.postal_object import PostalObject
from ..models.sender import Sender
import qrcode


class Tag:
    def __init__(self, sender, postal_object):
        if not isinstance(sender, Sender):
            raise Exception(
                'parameter sender is not valid. Must have be Sender instance')

        # if not isinstance(recipient, Recipient):
        #     raise Exception(
        #         'parameter recipient is not valid. Must have be Recipient instance')

        if not isinstance(postal_object, PostalObject):
            raise Exception(
                'parameter postal_object is not valid. Must have be PostalObject instance')

        # make qrcode
        qr_image = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr_image.add_data('CEP destino {}'.format(postal_object.nacional.cep_destinatario))
        qr_image.add_data('Complemento do CEP {}'.format(postal_object.destinatario.numero_end_destinatario))
        qr_image.add_data('CEP Origem {}'.format(sender.cep_remetente))
        qr_image.add_data('Complemento do CEP {}'.format(sender.numero_remetente))
        qr_image.add_data('Validador do CEP Destino {}'.format(postal_object.nacional.cep_destinatario))
        qr_image.add_data('IDV {}'.format(51))
        qr_image.add_data('Etiqueta {}'.format(postal_object.numero_etiqueta))
        qr_image.add_data('Serviços Adicionais {}'.format(postal_object.servico))
    
    @staticmethod
    def normalizeAdditionalServices(services):
        pass