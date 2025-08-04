# calculadora.py
import math
class Calculadora:
    def suma(self, a, b):
        """Suma dos números"""
        return a + b # retorna la suma: by Moises

    def resta(self, a, b):
        """Resta dos números"""
        pass

    def multiplicacion(self, a, b):
        """Multiplica dos números"""
        pass

    def division(self, a, b):
        """Divide dos números"""
        pass

    def potencia(self, base, exponente):
        """Calcula la potencia de un número"""
        pass

    def raiz_cuadrada(self, a):
        """Calcula la raíz cuadrada de un número"""
        if a < 0:
            return "Error: No se puede calcular la raíz cuadrada de un número negativo."
        return math.sqrt(a) #retorna la raiz cuadrada de a : by Alexis

    def modulo(self, a, b):
        """Calcula el módulo (resto) de la división"""
        pass

    def logaritmo(self, a, base=10):
        """Calcula el logaritmo de un número con base 10 por defecto"""
        pass

    def valor_absoluto(self, a):
        """Devuelve el valor absoluto de un número"""
        pass

    def maximo(self, a, b):
        """Devuelve el número mayor entre dos"""
        pass


def main():
    calc = Calculadora()
    print("Calculadora lista para implementar funciones.")


if __name__ == "__main__":
    main()
