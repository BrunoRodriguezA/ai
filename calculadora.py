#!/usr/bin/env python3
"""
Calculadora simple en Python
"""

def sumar(a, b):
    """Suma dos números"""
    return a + b


def restar(a, b):
    """Resta dos números"""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b


def dividir(a, b):
    """Divide dos números"""
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b


def potencia(a, b):
    """Calcula la potencia de un número"""
    return a ** b


def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "="*40)
    print("       CALCULADORA")
    print("="*40)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Salir")
    print("="*40)


def main():
    """Función principal de la calculadora"""
    while True:
        mostrar_menu()
        
        opcion = input("\nSelecciona una opción (1-6): ")
        
        if opcion == "6":
            print("\n¡Hasta luego!")
            break
        
        if opcion not in ["1", "2", "3", "4", "5"]:
            print("\nOpción inválida. Por favor, elige una opción del 1 al 6.")
            continue
        
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            if opcion == "1":
                resultado = sumar(num1, num2)
                print(f"\nResultado: {num1} + {num2} = {resultado}")
            elif opcion == "2":
                resultado = restar(num1, num2)
                print(f"\nResultado: {num1} - {num2} = {resultado}")
            elif opcion == "3":
                resultado = multiplicar(num1, num2)
                print(f"\nResultado: {num1} × {num2} = {resultado}")
            elif opcion == "4":
                resultado = dividir(num1, num2)
                print(f"\nResultado: {num1} ÷ {num2} = {resultado}")
            elif opcion == "5":
                resultado = potencia(num1, num2)
                print(f"\nResultado: {num1} ^ {num2} = {resultado}")
        
        except ValueError:
            print("\nError: Por favor, ingresa números válidos.")
        except Exception as e:
            print(f"\nError: {e}")
        
        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    main()
