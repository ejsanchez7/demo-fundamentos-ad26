from math import pi

# Operación para convertir kilómetros a millas
def convertir_km_millas(km) :
    return km / 1.609

# Operación para convertir grados a radianes
def convertir_grados_radianes(grados) :
    return grados * pi / 180

km = float(input("Escribe los kilómetros:"))
grados = float(input("Escribe los grados:"))

print(convertir_km_millas(km))
print(convertir_grados_radianes(grados))