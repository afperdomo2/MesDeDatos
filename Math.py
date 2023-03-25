from math import ceil, floor

# Uso de operaciones matemáticas

seconds = 1042
# División de múltiplo inferior = `//`
display_minutes = 1042 // 60
display_seconds = 1042 % 60

print("Minutos:", display_minutes)
print("MOD segundos:", display_seconds)

# Conversión de cadenas en números
print("\nFormateo de strings:", int('215'))
print("Formateo de strings:", float('215.3'))

# Valores abolutos
print("\nAbsoluto:", abs(39 - 16))
print("Absoluto:", abs(16 - 39))

# Redondeo
print("\nRedondeo:", round(14.5))

print("Redondear hacia arriba:", ceil(12.5))
print("Redondear hacia abajo:", floor(12.5))


# Ejercicio: calcular las distancias entre planetas
print("\n🌎 Ejercicio: Calular la distancia entre planetas🪐")
first_planet_input = input(
    "➡️  Enter the distance from the sun for the first planet in KM:")
second_planet_input = input(
    "➡️  Enter the distance from the sun for the second planet in KM:")

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

distance_km = second_planet - first_planet
print("Distance:", abs(distance_km), "km")
