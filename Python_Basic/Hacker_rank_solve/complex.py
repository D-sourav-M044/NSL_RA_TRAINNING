import math

class ComplexNo(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return ComplexNo(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return ComplexNo(real, imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return ComplexNo(real, imaginary)

    def __div__(self, no):
        x = float(no.real ** 2 + no.imaginary ** 2)
        y = self * ComplexNo(no.real, -no.imaginary)
        real = y.real / x
        imaginary = y.imaginary / x
        return ComplexNo(real, imaginary)

    def mod(self):
        real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return ComplexNo(real, 0)
# can also use __repr__ in place of __str__
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f" % (self.real)
        elif self.real == 0:
            result = "%.2fi" % (self.imaginary)
        elif self.imaginary > 0:
            result = "%.2f + %.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f - %.2fi" % (self.real, abs(self.imaginary))
        return result


