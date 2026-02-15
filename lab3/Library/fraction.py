import math

class Fraction:
    def __init__(self,numenator,denominator):
        if denominator == 0:
            raise ValueError('Value cannot be 0')
        
        # normalizing sign
        if denominator < 0:
            numenator = -numenator
            denominator = -denominator
        
        # reduce fraction
        gcd = math.gcd(numenator,denominator)
        self.n = numenator // gcd
        self.d = denominator // gcd

    def __str__(self):
        return f"{self.n}/{self.d}"
    
    def __repr__(self):
        return f"{self.n}/{self.d}"
    
    def __add__(self,other):
        numenator = self.n*other.d + self.d*other.n
        denominator = self.d*other.d

        return Fraction(numenator=numenator,denominator=denominator)
    
    def __sub__(self,other):
        numenator = self.n*other.d - self.d*other.n
        denominator = self.d*other.d

        return Fraction(numenator=numenator,denominator=denominator)
    
    def __mul__(self,other):
        numenator = self.n*other.n
        denominator = self.d*other.d

        return Fraction(numenator=numenator,denominator=denominator)

    def __truediv__(self, other):
        if other.n == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction")
        numerator = self.n * other.d
        denominator = self.d * other.n

        return Fraction(numenator=numerator,denominator=denominator)
    
    def __eq__(self,other):
        return self.n == other.n and self.d == other.d
    