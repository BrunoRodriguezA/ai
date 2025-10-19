#!/usr/bin/env python3
"""
Spanish greeting module
"""

def send_spanish_greeting(name="amigo"):
    """
    Send a Spanish greeting to someone
    
    Args:
        name: The name of the person to greet (default: "amigo")
    
    Returns:
        A Spanish greeting message
    """
    return f"¡Hola, {name}! ¿Cómo estás?"


def main():
    """Main function to demonstrate Spanish greeting"""
    print(send_spanish_greeting())
    print(send_spanish_greeting("María"))
    print(send_spanish_greeting("Juan"))


if __name__ == "__main__":
    main()
