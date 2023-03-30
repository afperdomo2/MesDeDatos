#  Aspectos básicos de las cadenas en Python
fact = 'The "Moon" has no atmosphere.'

# Comillas triples:
# - Permite agregar "" y '' en el String
# - Permite realizar texto multilínea
fact += """No sound 'can' be heard on the "Moon".

Facts about the Moon:
- There is no atmosphere.
- There is no sound."""

print("\n" + fact)
print(type(fact))

# Métodos de cadena en Python
print("i like play voley".title())
moon = "temperatures and facts about the moon"
print(moon.title())

# División de una cadena
temperatures = """Daylight: 260 F
Nighttime: -280 F"""
print(temperatures.split())
print(temperatures.split("\n"))

# Búsqueda de una cadena
if "Moon" in "This text will describe facts about the Moon":
    print("\nExist the moon 🌖")

# Devuelve el índice de dónde se encontró la cadena. -1 Si no la encuentra
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius.""".lower()
print("\nFound index:", temperatures.find("TEMPERATURE".lower()))

# Total de repeticiones de la cadena buscada
print("\nCount:", temperatures.count("Celsius".lower()))

temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(":")
print("🌡️  Temp:", parts[1].strip())  # strip => trim
print("🌡️  Temp:", parts[-1])  # -1 = Último elemento de la lista

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print("🌡️  Mars temperature:", item)

if "30 C".endswith("C"):
    print("This temperature is in Celsius")

# Reemplazar texto
saturn = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."
print(saturn.replace("Celsius", "°C"))

if "saturn" in saturn.lower():
    print("\n🪐 Found Saturn")

# Convertir elementos de un iterable en un string
moon_facts = ["The Moon is drifting away from the Earth.",
              "On average, the Moon is moving about 4cm every year"]
print("\n🌖 Moon facts:", "".join(moon_facts))

# Incluir variables en los prints
mass_percentage = "1/6"
print("\n🚀 Replace vars: On the Moon, you would weigh about %s of your weight on Earth" %
      mass_percentage)

# Incluir más de una variable en los prints
print("""\n⚠️  Texto con múltiples variables:
Both sides of the %s get the same amount of sunlight,
but only one side is seen from %s because
the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

# Reemplazando con format(). Usa {} como marcador
mass_percentage = "1/6"
print("\n🚀 Format():", "On the Moon, you would weigh about {} of your weight on Earth".format(
    mass_percentage))

# No es necesario asignar variables repetidas varias veces, lo que hace
# que sea menos detallado porque es necesario asignar menos variables:
print("""\n🚀 Format() con múltiples variables:
You are lighter on the {0}, because on the {0}
you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))

print("""\n🚀 Format() usando referencias:
You are lighter on the {moon}, because on the {moon}
you would weigh about {mass} of your weight on Earth""".format(moon="Moon🌖", mass=mass_percentage))

# Cadenas f-strings
# A partir de la versión 3.6 de Python, es posible usar f-strings. Estas cadenas
# parecen plantillas y usan los nombres de variable del código. El uso de
# f-strings en el ejemplo anterior tendría el siguiente aspecto:
print("\n🧪 f-strings:",
      f"On the Moon, you would weigh about '{mass_percentage}' of your weight on Earth")
print("\n🧪 f-strings:",
      f"On the Moon, you would weigh about {round(100/6, 1)}% of {'your weight on Earth'.upper()}")
