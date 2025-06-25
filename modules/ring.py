class Ring:
    def __init__(self, modulo=None, elements=None, add_table=None, mul_table=None):
        self.is_modulo = modulo is not None
        if self.is_modulo:
            self.n = modulo
            if(modulo <= 0): raise Exception("modulo should be a natural number")
            self.elements = list(range(self.n))
        else:
            self.elements = elements
            self.add_table = add_table
            self.mul_table = mul_table

    def add(self, a, b):
        if self.is_modulo:
            return (a + b) % self.n
        else:
            return self.add_table[self.elements.index(a)][self.elements.index(b)]

    def mul(self, a, b):
        if self.is_modulo:
            return (a * b) % self.n
        else:
            return self.mul_table[self.elements.index(a)][self.elements.index(b)]
