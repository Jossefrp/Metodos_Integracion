from sympy import *


class NewtonCotes:

    def __init__(self, a=0, b=0, f=0, h=0):
        self._a = a
        self._b = b
        self._funcion = f
        self._h = h

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        self._b = b

    @property
    def funcion(self):
        return self._funcion

    @funcion.setter
    def funcion(self, f):
        self._funcion = f

    @property
    def h(self):
        return self._h

    @staticmethod
    def subdivisiones(multiplo):
        try:
            n = int(input("Ingrese el numero de subdivisiones: "))
            assert n % int(multiplo) == 0
            return n
        except AssertionError:
            print("El numero de subdivisiones tiene que ser multiplo de: ", multiplo)
            raise KeyboardInterrupt

    def maximo_derivada(self, n):
        variable = list(self._funcion.free_symbols)[0]
        derivada_funcion = abs(diff(self._funcion, variable, n))
        maximo = derivada_funcion.subs(variable, self._b) if derivada_funcion.subs(variable, self._b) > \
            derivada_funcion.subs(variable, self._a) else derivada_funcion.subs(variable, self._a)
        return maximo

    def error(self, h, n, divisiones):
        t = Symbol("t")
        terminos = 1
        for i in range(n + 1):
            terminos *= t - i
        if n % 2 == 0:
            maximo = NewtonCotes.maximo_derivada(self, n + 2)
            terminos *= t
            error_aprox = h**(n + 3)/factorial(n + 2) * maximo * abs(integrate(terminos, (t, 0, n))) * divisiones/n
        else:
            maximo = NewtonCotes.maximo_derivada(self, n + 1)
            error_aprox = h**(n + 2)/factorial(n + 1) * maximo * abs(integrate(terminos, (t, 0, n))) * divisiones/n
        return error_aprox.evalf(8)

    def trapecio(self, variable):
        aproximacion = lambda a0, b: self._funcion.subs(variable, a0) + self._funcion.subs(variable, b)
        suma, i = 0, self._a
        particiones = NewtonCotes.subdivisiones(1)
        h = (self._b - self._a)/particiones
        self._h = h
        for j in range(int(particiones)):
            a = i
            i += h
            suma += aproximacion(a, i)
        valor_aproximado = h/2 * suma
        return valor_aproximado.evalf(8), particiones

    def simpson13(self, variable):
        aproximacion = lambda a0, b: self._funcion.subs(variable, a0) + 4 * self._funcion.subs(variable, (a0 + b) / 2) \
                                     + self._funcion.subs(variable, b)
        suma, i = 0, self._a
        particiones = NewtonCotes.subdivisiones(2)
        h = (self._b - self._a)/particiones
        self._h = h
        for j in range(int(particiones/2)):
            a = i
            i += 2*h
            suma += aproximacion(a, i)
        valor_aproximado = h/3 * suma
        return valor_aproximado.evalf(8), particiones

    def simpson38(self, variable):
        aproximacion = lambda a0, b: self._funcion.subs(variable, a0) + 3*self._funcion.subs(variable, (2*a0 + b)/3)\
                                     + 3*self._funcion.subs(variable, (a0+2*b)/3) + self._funcion.subs(variable, b)
        suma, i = 0, self._a
        particiones = NewtonCotes.subdivisiones(3)
        h = (self._b - self._a)/particiones
        self._h = h
        for j in range(int(particiones/3)):
            a = i
            i += 3*h
            suma += aproximacion(a, i)
        valor_aproximado = 3/8 * h * suma
        return valor_aproximado.evalf(8), particiones

    def boole(self, variable):
        particiones = NewtonCotes.subdivisiones(4)
        aproximacion = lambda a0, b: 7 * self._funcion.subs(variable, a0) + 32 * self._funcion.subs(variable, a0 + h) \
                            + 12 * self._funcion.subs(variable, a0 + 2 * h) + 32 * self._funcion.subs(variable, a0+3*h)\
                            + 7 * self._funcion.subs(variable, b)

        suma, i = 0, self._a
        h = (self._b - self._a)/particiones if self._h == 0 else self._h
        self._h = h
        for j in range(int(particiones/4)):
            a = i
            i += 4*h
            suma += aproximacion(a, i)
        valor_aproximado = 4/90 * h * suma
        return valor_aproximado.evalf(8), particiones
