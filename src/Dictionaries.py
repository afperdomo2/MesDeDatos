# 1. Diccionarios de datos

planet = {
    'name': 'Earth',
    'moons': 1
}
print("Planeta:", planet)


# Leer valores
print("\n- Leer:")
print("Nombre:", planet.get("name"))
print("Nombre:", planet["name"])

print("Nombre:", planet.get("gravity"))  # Si no existe, devuelve None
# print("Nombre:", planet["gravity"]) # Si no existe, devuelve error


# Modificar valores
print("\n- Actualizar:")
# Actualizar un valor
planet.update({'name': 'Mars'})
planet["moons"] = 2
print(planet)

# Actualizar el diccionario completo
planet.update({
    'name': 'Jupiter',
    'moons': 79
})
print(planet)


# Agregar una clave
print("\n- Adicionar:")
planet['orbital period'] = 4333
print(planet)


# Eliminar una clave
print("\n- Eliminar:")
planet.pop("orbital period")
print(planet)


# Tipos de data complejos
print("\n- Tipos de data complejos:")
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(planet)

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')


# 2. Programación dinámica con diccionarios
print("\n")
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
# Recorrer un diccionario
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')


if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

print("\n", rainfall)


# Recuperación de todos los valores
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'\nThere was {total_rainfall}cm in the last quarter')
