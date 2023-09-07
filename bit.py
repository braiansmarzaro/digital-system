class Bit:
    def __init__(self, bitvalue):
        if bitvalue in [0, 1, "x"]:
            self._value = bitvalue
            return
        raise ValueError("Os possíveis valores para o argumento 'bitvalue' são 0, 1 e 'x'.")

    def __invert__(self):
        if self._value == 1:
            return Bit(0)
        if self._value == 0:
            return Bit(1)
        return Bit("x")
    
    def __or__(self, other):        
        if self._value == 1 or other._value == 1:
            return Bit(1)
        elif self._value == 0:
            return Bit(other._value)
        elif other._value == 0:
            return Bit(self._value)
        return Bit("x")
    __add__ = __or__

    def __and__(self, other):
        if isinstance(other,bool):
            other=Bit(int(other))
        if self._value == 0 or other._value == 0:
            return Bit(0)
        elif self._value == 1:
            return Bit(other._value)
        elif other._value == 1:
            return Bit(self._value)
        return Bit("x")
    
    __mul__= __and__

    def __xor__(self, other):
        if isinstance(other,bool):
            other=Bit(int(other))
        if self._value == "x" or other._value == "x":
            return Bit("x")
        elif self._value == other._value:
            return Bit(0)
        return Bit(1)

    def __str__(self):
        return str(self._value)
    
    def __repr__(self):
        return f"Bit({self._value})"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, bitvalue):
        if bitvalue in [0, 1, "x"]:
            self._value = bitvalue
            return
        raise ValueError("Os possíveis valores para 'value' são 0, 1 e 'x'.")

if __name__=='__main__':
    a = Bit(1)
    b = Bit(0)
    c = Bit("x")
    print(a+b)
    print(a or b)
    print(a*b and c)
    print(a^b)
    print(~~a)
