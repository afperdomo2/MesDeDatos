# Uso de listas

planets = ["Mercury", "Venus", "Earth", "Mars",
           "Jupiter", "Saturn", "Uranus", "Neptune"]
planets[0] = "Mercurio"

print("🌏 The first planet is:", planets[0])
print("🌏 The second planet is:", planets[1])
print("🌏 The third planet is:", planets[2])

print("\nCantidad de planetas:", len(planets))


# Incorporar un valor a la lista
planets.append("Pluto")
print("\nPlanetas:", planets)
print("Cantidad de planetas:", len(planets))


# Borrar el último valor de la lista
planets.pop()
print("\nPlanetas:", planets)
print("Cantidad de planetas:", len(planets))

print("\nThe first planet is", planets[0])
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])


# Búsqueda de un valor en una lista
saturn_index = planets.index("Saturn")
print("\n🪐 Saturn is the", saturn_index + 1, "planet from the sun")


# Listas de números
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
print("\n🏋️  Gravity on planets:", gravity_on_planets)

print(f"\n🪐 Saturn's Gravity: {gravity_on_planets[saturn_index]} G")


# Valor mínimo y máximo de una lista
print("\nMin gravity:", min(gravity_on_planets), "G")
print("Max gravity:", max(gravity_on_planets), "G")


# Segmentar listas
planets = ["Mercury", "Venus", "Earth", "Mars",
           "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print("\nPlanets before earth:", planets_before_earth)

planets_after_earth = planets[3:8]
# Si no se pone el segundo índece, se asume el último
planets_after_earth = planets[3:]
print("Planets after earth:", planets_after_earth)


# Combinación de listas
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("\n🌘  The regular satellite moons of Jupiter are:", regular_satellite_moons)


# Ordenación de listas.
# sort() = Modifica la lista actual
regular_satellite_moons.sort()
print("\n🌘  Moons of Jupiter:", regular_satellite_moons)
regular_satellite_moons.sort(reverse=True)
print("\n🌘  Moons of Jupiter (reverse):", regular_satellite_moons)
