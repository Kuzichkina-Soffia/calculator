#калькулятор
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self,x,y):
        return self.x+self.y
    
    def subtraction(self,x,y):
        return(x-y)
    
    def multiplication(self,x,y):
        return(x*y)
    
    def division(self,x,y):
        return(x/y)
    
    def exponentiation(self,x,y):
        return(x**y)