print(1+2)
print("abc" + "def")
print([1, 2, 4] + [1,2,3] )

# also known as a Dunder functions. wher you see two undersoucer "__"
# complex numebr

class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image
        
    def show(self):
        print(self.real,"i +", self.image,"j")
    
    def add(self, num2):
        newReal = self.real + num2.real
        newImage = self.image + num2.image
        return Complex(newReal, newImage)
    
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImage = self.image + num2.image
        return Complex(newReal, newImage)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImage = self.image - num2.image
        return Complex(newReal, newImage)

    def __mul__(self, num2):
        newReal = self.real * num2.real
        newImage = self.image * num2.image
        return Complex(newReal, newImage)
    
print("======================")
    
c = Complex(1,3)
c.show()
       

c2 = Complex(4,7)
c2.show()
print("======================")
c3 = c.add(c2)

c3.show()
c4 = c3 - c
c.show()
print("======================")
c4.show()

c2.show()
print("======================")
c5 = c4 * c2
c5.show()

