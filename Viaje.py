import geopy.distance
import time

# Diccionario con las coordenadas aproximadas de algunas ciudades de Chile y Argentina
ciudades = {
    "santiago": (-33.4489, -70.6693),
    "buenos aires": (-34.6037, -58.3816),
    "valparaiso": (-33.0472, -71.6127),
    "mendoza": (-32.8895, -68.8458)
}

def obtener_coordenadas(ciudad):
    return ciudades.get(ciudad.lower())

def calcular_distancia(ciudad_origen, ciudad_destino):
    coords_origen = obtener_coordenadas(ciudad_origen)
    coords_destino = obtener_coordenadas(ciudad_destino)
    if not coords_origen or not coords_destino:
        return None
    return geopy.distance.distance(coords_origen, coords_destino).km

def calcular_duracion(distancia, velocidad):
    return distancia / velocidad

def mostrar_narrativa(ciudad_origen, ciudad_destino, distancia, duracion, transporte):
    print(f"\nNarrativa del viaje:")
    print(f"El viaje desde {ciudad_origen.capitalize()} hasta {ciudad_destino.capitalize()} cubre una distancia de {distancia:.2f} km.")
    print(f"En {transporte}, este viaje tomará aproximadamente {duracion:.2f} horas.\n")

def main():
    while True:
        ciudad_origen = input("Ingrese la Ciudad de Origen (o 's' para salir): ")
        if ciudad_origen.lower() == 's':
            break
        ciudad_destino = input("Ingrese la Ciudad de Destino: ")

        distancia_km = calcular_distancia(ciudad_origen, ciudad_destino)
        if distancia_km is None:
            print("Una o ambas ciudades no están en la base de datos. Intente nuevamente.")
            continue

        distancia_millas = distancia_km * 0.621371

        print("Seleccione el medio de transporte:")
        print("1. Automóvil (100 km/h)")
        print("2. Autobús (80 km/h)")
        print("3. Bicicleta (15 km/h)")
        medio_transporte = input("Ingrese el número del medio de transporte: ")

        if medio_transporte == '1':
            velocidad = 100
            transporte = "automóvil"
        elif medio_transporte == '2':
            velocidad = 80
            transporte = "autobús"
        elif medio_transporte == '3':
            velocidad = 15
            transporte = "bicicleta"
        else:
            print("Opción no válida. Intente nuevamente.")
            continue

        duracion = calcular_duracion(distancia_km, velocidad)

        print(f"\nDistancia: {distancia_km:.2f} km ({distancia_millas:.2f} millas)")
        print(f"Duración estimada del viaje: {duracion:.2f} horas\n")

        mostrar_narrativa(ciudad_origen, ciudad_destino, distancia_km, duracion, transporte)

if __name__ == "__main__":
    main()
