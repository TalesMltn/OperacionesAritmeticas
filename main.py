from OperaciomesAritmeticas import OperaciomesAritmeticas


if __name__=='__main__':
    operación = OperaciomesAritmeticas()
    num1, num2 = operación.ingresoNumeros()
    print(f"{num1} + {num2}= {operación.suma(num1, num2)}")

