from ..correios_sigep.utils.etree import parseDict
from lxml import etree

def test_xml_parse_dict():
    a = {
        'singevlue': 123,
        'dict': {
            'singlevalue': 456,
            'oto': 1
        }
    }

    print etree.tostring(parseDict(a, 'correioslog'), pretty_print=True)

    assert(1==2)