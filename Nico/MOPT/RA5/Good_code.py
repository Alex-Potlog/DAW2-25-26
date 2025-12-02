# Imports no utilitzats
# import os, sys, math, json
# from math import *
PI = 3.14159


class Calculator:
    '''Classe per fer operacions bàsiques de càlcul.'''

    def __init__(self, name):
        '''Constructor de la classe'''
        self.name = name

    def add(self, a, b):
        '''Retorna la suma de dos nombres.'''
        return a + b


def compute_circle_area(radius):
    '''Calcula l'àrea d'un cercle a partir del radi.'''
    return PI * radius * radius


def print_info(calc):
    '''Mostra informació sobre la calculadora.'''
    print("Calculator:", calc.name)


def divide(a, b):
    '''Divideix dos nombres, retorna None si el divisor és 0.'''
    if b == 0:
        return None
    return a / b


def main():
    '''Funció principal.'''
    calc = Calculator("Prova")
    print_info(calc)
    print("Area:", compute_circle_area(5))
    print("Sum:", calc.add(2, 3))
    print("Div:", divide(4, 2))


if __name__ == "__main__":
    main()
