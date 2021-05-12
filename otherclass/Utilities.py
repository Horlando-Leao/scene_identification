from urllib.request import urlopen


class Utilities:
    def __init__(self):
        self.serial = 1

    def truncate_number(self, value, decimal_places):
        """ Trunca / preenche um flutuante f para n casas decimais sem arredondamento """

        s = '{}'.format(value)
        if 'e' in s or 'E' in s:
            return '{0:.{1}f}'.format(value, decimal_places)
        i, p, d = s.partition('.')

        return '.'.join([i, (d + '0' * decimal_places)[:decimal_places]])

    def valid_url(url_valid: str = False) -> bool:
        """VALIDA A DISPONIBILIDADE DO SERVIDOR"""
        #print(url_valid)
        try:
            if isinstance(url_valid, str):
                url = urlopen(url_valid)
                #print(url)
                return True
            else:
                return False
        except Exception as e:
            # print("Servidor indisponível. Erro:", e)
            return False


#print(Utilities.valid_url("https://i.ytig.com/vi/LKlH9Cdi_oA/maxresdefault.jpg"))
