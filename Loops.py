from time import sleep

# Uso de bucles "while" y "for" en Python


# 1. For
print("- Loop For:")
countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")


# 2. While
print("\n- Loop While:")
new_planet = ''
planets = []

while new_planet.lower() != 'done':
    # Si viene un input del usuario, se almacena
    if new_planet:
        planets.append(new_planet)
    # Realiza el input
    new_planet = input('➡️  Enter a new planet, or done when done:')

print("🪐 Planets:", planets)

for planet in planets:
    print("Planet:", planet)