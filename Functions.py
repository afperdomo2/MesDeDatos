from datetime import timedelta, datetime

# 1. Aspectos básicos de las funciones de Python
print("\n1 - Aspectos básicos de las funciones de Python:")


# Funciones sin argumentos
def rocket_parts():
    return "payload, propellant, structure"


output = rocket_parts()
print(output)

# Argumentos opcionales y requeridos
print(any([True, False, False]))
print(any([False, False, False]))
# print(any()) # Requiere almenos un argumento, genera error


# Exigencia de un argumento
def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"


print("\nDistance:", distance_from_earth("Moon"))
print("Distance:", distance_from_earth("Saturn"))


# Varios argumentos necesarios
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24


total_days = days_to_complete(238855, 75)
print("\nDays to complete:", total_days)
print("Days to complete:", round(total_days))


# 2. Uso de argumentos de palabra clave en Python
def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")


print("\n2 - Uso de argumentos de palabra clave en Python:")
print(arrival_time())
print(arrival_time(hours=0))


# Combinación de argumentos y argumentos de palabra clave
def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")


print(arrival_time("Moon"))
print(arrival_time("Orbit", hours=0.13))


# 3. Uso de argumentos de variable en Python
print("\n3 - Uso de argumentos de variable en Python:")


# Argumentos de variable
def variable_length(*args):
    print(args)


variable_length(2, 4, 5)
variable_length("one", "two")


def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"


print("\nSecuence:", sequence_time(4, 14, 18))
print("Secuence:", sequence_time(4, 14, 48))


# Argumentos de palabra clave variable
def variable_length(**kwargs):
    print(kwargs)


variable_length(tanks=1, day="Wednesday", pilots=3)


def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")


print("\n")
crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin",
             command_pilot="Michael Collins")
