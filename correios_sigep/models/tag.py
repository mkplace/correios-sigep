class Tag:
    
    def __init__(self, tag):
        self._tag = tag
        self._tag_w_digit = ''
        self._dv = ''

    @property
    def tag(self):
        return self._tag

    @property
    def tag_w_digit(self):
        if len(self._tag_w_digit) == 13 and self._tag_w_digit[10:11] == '':
            raise Exception('dv is not present')
        else:
            return self._tag_w_digit

    def setDv(self, dv):
        if not dv:
            raise Exception('Invalid DV')
        self._tag_w_digit = self._tag.replace(' ', dv)
        self._dv = dv
    
    @property
    def dv(self):
        return self._dv

    @staticmethod
    def clean(tag):
        return tag.replace(' ', '')

    def generate_dv(self):
        prefix = self._tag[:2]
        number = self._tag[2:11]
        sufix = self._tag[11:13].strip()
        ret = number.ljust(8, '0')[:8]

        map(lambda(i,v): i*int(v) , enumerate(list(ret)))

        