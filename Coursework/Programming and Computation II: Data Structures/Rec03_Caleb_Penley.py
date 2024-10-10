class Complex:
    """ Complex number of the form a + bi, where a and b are real numbers, and i is an indeterminate satisfying i**2 = −1 """

    def __init__(self,r,i):
        self._real = r
        self._imag = i
    
    def __str__(self):
        """Display Complex number"""
        if self._imag>=0:
           return f"{self._real} + {self._imag}i"    # This is a string representation of the Complex object, not a Complex object
        else:
           return f"{self._real} - {abs(self._imag)}i"
    
    __repr__ = __str__  

    def conjugate(self):
        """Returns a Complex object that represents the Complex conjugate"""
        return Complex(self._real, -self._imag)
    
    def __mul__(self,other):
        """Multiply two Complex numbers"""
        if not isinstance(other, Complex):
            real_part = (self._real * other )    # Value for the real part
            imag_part = (self._imag * other)   # Value for the imaginary part
            ans =  Complex(real_part, imag_part)
        elif not isinstance(self, Complex):
            real_part = (other._real * self)
            imag_part = (other._imag * self)
            ans = Complex(real_part, imag_part)
        else:
            real_part = (self._real * other._real- self._imag * other._imag )    # Value for the real part
            imag_part = (self._real * other._imag+self._imag * other._real )   # Value for the imaginary part
            ans =  Complex(real_part, imag_part)             # New instance of the class
        return ans
    
    def __rmul__(self,other):
        """Multiply a real and Complex number"""
        return self*other   
    
class Real(Complex):

    def __init__(self, value):
        super().__init__(value, 0)
    
    def __str__(self):
        """Display Complex number"""
        if self._imag>=0:
           return f"{self._real} + {self._imag}i"    # This is a string representation of the Complex object, not a Complex object
        else:
           return f"{self._real} - {abs(self._imag)}i"
    
    __repr__ = __str__ 

    def __mul__(self,other):
        if isinstance(self, Real) and isinstance(other,Real):
            out_num = (self._real * other._real)
            ans = Real(out_num)
        
        elif isinstance(other, (int,float)):
            if isinstance(self, Real):
                out_num = (self._real * other)
                ans = Real(out_num)
        elif isinstance(self, (int,float)):
            if isinstance(other, Real):
                out_num = (other._real * self)
                ans = Real(out_num)
        elif isinstance(other, Complex) or isinstance(self,Complex):
            real_part = (self._real * other._real- self._imag * other._imag )    # Value for the real part
            imag_part = (self._real * other._imag+self._imag * other._real )   # Value for the imaginary part
            ans =  Complex(real_part, imag_part) 
        return ans
    
    def __eq__(self,other):
        if isinstance(other, Real) and isinstance(self, Real):
            return self._real == other._real
        elif isinstance(other, Complex):
            return other._imag == 0 and other._real == self._real
        else:
            return False
    
    def __int__(self):
        return int(self._real)
    
    def __float__(self):
        return float(self._real)
    



