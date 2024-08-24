class Regla:
    def __init__(self, condiciones, conclusion):
        self.condiciones = condiciones
        self.conclusion = conclusion

def encadenamiento_hacia_adelante(hechos, reglas):
    conclusiones = set()
    nuevo_hecho_agregado = True

    while nuevo_hecho_agregado:
        nuevo_hecho_agregado = False

        for regla in reglas:
            if regla.condiciones.issubset(hechos) and regla.conclusion not in hechos:
                hechos.add(regla.conclusion)
                conclusiones.add(regla.conclusion)
                nuevo_hecho_agregado = True

    return conclusiones

def obtener_preferencias():
    hechos = set()
    genero = input("¿Cuál es tu género preferido (accion, drama, animacion, comedia, horror, ciencia ficcion)? ").strip().lower()
    hechos.add(genero)
    
    duracion = input("¿Prefieres películas cortas, medias o largas? ").strip().lower()
    hechos.add(duracion)
    
    return hechos

def mostrar_recomendaciones(conclusiones):
    if conclusiones:
        print("\nTe recomendamos ver:")
        for conclusion in conclusiones:
            print(f"- {conclusion}")
    else:
        print("Lo siento, no encontramos una película que coincida con tus preferencias.")

def main():
    reglas = [
        Regla({"accion", "larga"}, "Inception"),
        Regla({"drama", "larga"}, "Titanic"),
        Regla({"animacion", "corta"}, "Toy Story"),
        Regla({"accion", "media"}, "Mad Max: Fury Road"),
        Regla({"drama", "media"}, "The Pursuit of Happyness"),
        Regla({"comedia", "corta"}, "Superbad"),
        Regla({"horror", "larga"}, "The Conjuring"),
        Regla({"ciencia ficcion", "media"}, "Interstellar"),
        Regla({"comedia", "media"}, "The Hangover"),
        Regla({"horror", "media"}, "Get Out"),
        Regla({"accion", "corta"}, "John Wick: Chapter 1"),
        Regla({"ciencia ficcion", "larga"}, "Blade Runner 2049")
    ]
    
    while True:
        print("\nBienvenido")
    
        hechos = obtener_preferencias()

        conclusiones = encadenamiento_hacia_adelante(hechos, reglas)
        
        mostrar_recomendaciones(conclusiones)

        respuesta = input("\n¿Quieres hacer otra búsqueda? (si/no): ").strip().lower()
        if respuesta != 'si':
            print("Gracias por usar el sistema.")
            break

if __name__ == "__main__":
    main()
