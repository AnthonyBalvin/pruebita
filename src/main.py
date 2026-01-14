# He dejado este 'import os' a propósito. No se usa,
# por lo que el "linter" (Ruff) debería quejarse más adelante.
import os

def saludar(nombre):
    """Devuelve un saludo simple."""
    if not nombre:
        return "Hola, desconocido!"
    return f"Hola, {nombre}!"

if __name__ == "__main__":
    print(saludar("Mundo"))