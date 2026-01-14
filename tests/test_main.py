import pytest
from src.main import saludar

def test_saludo_con_nombre():
    """Prueba que el saludo funcione con un nombre dado."""
    resultado = saludar("Emilio")
    assert resultado == "Hola, Emilio!"

def test_saludo_sin_nombre():
     """Prueba que funcione cuando se pasa cadena vacia"""
     resultado = saludar("")
     assert resultado == "Hola, desconocido!"