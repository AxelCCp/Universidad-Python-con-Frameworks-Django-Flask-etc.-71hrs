class Aritmetica:

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB
    
    def mult(self):
        return self.operandoA * self.operandoB
    
    def div(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(5,3)

print(f'SUMA : {aritmetica1.sumar()}')

print(f'RESTA : {aritmetica1.restar()}')

print(f'MULTIPLICAR : {aritmetica1.mult()}')

print(f'DIVIDIR : {aritmetica1.div():.4f}')
