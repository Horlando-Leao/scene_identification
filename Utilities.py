class Utilities:

    def truncate_number(value, decimal_places):
        """ Trunca / preenche um flutuante f para n casas decimais sem arredondamento """

        s = '{}'.format(value)
        if 'e' in s or 'E' in s:
            return '{0:.{1}f}'.format(value, decimal_places)
        i, p, d = s.partition('.')

        return '.'.join([i, (d + '0' * decimal_places)[:decimal_places]])


print(Utilities.truncate_number(value=1212.1222212, decimal_places=0))
