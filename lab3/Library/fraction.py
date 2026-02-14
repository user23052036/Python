class Fraction:

    def __init__(self,numenator,denominator):
        self.n = numenator 
        self.d = denominator

    def __str__(self):
        return "{}/{}".format(self.n,self.d)
    
    def __repr__(self):
        return f"{self.n}/{self.d}"
    
    def __add__(self,other):
        numinator = self.n*other.d + self.d*other.n
        denominator = self.d*other.d

        new_fraction = Fraction(numenator=numinator,denominator=denominator)
        return new_fraction
    