from fractions import Fraction

class Fraction_cls:
    def __init__(self,x):
        x=x.split("/")
        self.x=Fraction(int(x[0]))/Fraction(int(x[1]))

    def __add__(self, other):
        return self.x+other.x
        # return str((int(self.x[0])*int(other.x[1]))+(int(other.x[0])*int(self.x[1])))+"/"+str(int(self.x[1])*int(other.x[1]))

    def __truediv__(self, other):
        return other.x/self.x

    def __sub__(self, other):
        return self.x-other.x

    def __mul__(self, other):
        return self.x*other.x


x=Fraction_cls("1/2")
y=Fraction_cls("2/5")
print(x+y)
print(x-y)
print(x*y)
print(x/y)
