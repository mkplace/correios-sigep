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

def test_verifica_disponibilidade_cartao_postagem():
    client = Client('74558537000', '4wvp84', 'sigep-production')

    params = {
        'postcard_number': '0072501197'
    }
    result = client.get_postcard_status(**params)
    print result
    assert(1==2)