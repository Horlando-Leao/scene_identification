class Foo:

    def __init__(self, ifood):
        self.ifood = ifood

    @property
    def ifood(self):
        return self._ifood

    @ifood.setter
    def ifood(self, value):
        if not (isinstance(value, int)):
            raise AttributeError(f'ifood not attribute for {type(value)}, but for {int}')
        if not (value >= 1):
            raise ValueError(f'ifood need to value > 1')
        self._ifood = value


teste = Foo(111)

print(teste.ifood)
teste.ifood = 1
print(teste.ifood)
teste.ifood = 0.1
print(teste.ifood)
teste.ifood = 0
print(teste.ifood)