from NewtonCotes import NewtonCotes
from sympy import Symbol, sympify
from colorama import init, Fore, Style


def titulo():
    init()
    print(Fore.YELLOW + Style.BRIGHT + """
| \ | |             | |                  /  __ \     | |           
|  \| | _____      _| |_ ___  _ __ ______| /  \/ ___ | |_ ___  ___ 
| . ` |/ _ \ \ /\ / / __/ _ \| '_ \______| |    / _ \| __/ _ \/ __|
| |\  |  __/\ V  V /| || (_) | | | |     | \__/\ (_) | ||  __/\__ \\
\_| \_/\___| \_/\_/  \__\___/|_| |_|      \____/\___/ \__\___||___/
                                By: JossefR
                                Github: https://github.com/Jossefrp
""")
    print(Style.RESET_ALL)


def main():
    x, y, z = Symbol('x'), Symbol('y'), Symbol('z')
    try:
        orden = int(input("Ingrese el orden de la integral (1 - 3): "))
        assert 0 < orden < 4
    except AssertionError:
        orden = 0
        raise KeyboardInterrupt

    f = sympify(input("Ingresa la función: "))
    aproximacion = NewtonCotes(f=f)
    for i in range(orden):
        print("\nIntegral ", i + 1)
        a = sympify(input("Ingrese el limite inferior: "))
        b = sympify(input("Ingrese el limite superior: "))
        variable = sympify(input("Ingrese la variable de integración: "))
        aproximacion.a = a
        aproximacion.b = b
        print("Ingrese el método de aproximación")
        print("1. Trapecio")
        print("2. Simpson(1/3)")
        print("3. Simpson(3/8)")
        print("4. Boole")
        metodo_aproximacion = int(input("--> "))
        print()
        if metodo_aproximacion == 1:
            nueva_funcion, divisiones = aproximacion.trapecio(variable)
            n = 1
            print("Aproximación trapecio: ", nueva_funcion)
        elif metodo_aproximacion == 2:
            nueva_funcion, divisiones = aproximacion.simpson13(variable)
            n = 2
            print("Aproximación Simpson(1/3): ", nueva_funcion)
        elif metodo_aproximacion == 3:
            nueva_funcion, divisiones = aproximacion.simpson38(variable)
            n = 3
            print("Aproximación Simpson(3/8): ", nueva_funcion)
        elif metodo_aproximacion == 4:
            nueva_funcion, divisiones = aproximacion.boole(variable)
            n = 4
            print("Aproximación Boole: ", nueva_funcion)
        else:
            n, divisiones = 0, 0
            nueva_funcion = 0
            print("Opción incorrecta")
            print("Finalizado")
            raise KeyboardInterrupt

        if orden == 1:
            print("Error estimado: ", aproximacion.error(aproximacion.h, n, divisiones))
        aproximacion.funcion = nueva_funcion


if __name__ == '__main__':
    try:
        titulo()
        main()

    except KeyboardInterrupt:
        print("Finalización forzosa")
    finally:
        print()
        input("Pulse enter para salir")
