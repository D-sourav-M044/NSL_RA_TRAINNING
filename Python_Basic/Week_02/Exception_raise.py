import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        real = int(self.real) + int(no.real)
        imaginary = int(self.imaginary) + int(no.imaginary)
        return Complex(real,imaginary)
        
    def __sub__(self, no):
        real = int(self.real) - int(no.real)
        imaginary = int(self.imaginary) - int(no.imaginary)
        return Complex(real,imaginary)
        

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    a,b = input().split()
    c,d =input().split()
    one = Complex(a,b)
    two = Complex(c,d)
    sum = one + two
    print(sum)
    sub = one -two
    print(sub)
    