def saludar(nombre):
    """Devuelve un saludo simple."""
    if not nombre:
        return "Hola, desconocido!"
    return f"Hola, {nombre}!"

if __name__ == "__main__":
    print(saludar("Mundo"))