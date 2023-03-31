# Control de errores de Python


# Capturando excepciones
def main():
    try:
        configuration = open('src/config2.txt')
    except FileNotFoundError as err:
        print("Couldn't find the config.txt file!", err)
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")


if __name__ == '__main__':
    main()


# Ejecercicio 1
def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypeError will be raised only if it isn't the right type
            # Raise the same exception but with a better error message
            raise TypeError(
                f"\n⛔ All arguments must be of type int, but received: '{type(argument)}'")

    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        # Generar una excepción controlada
        raise RuntimeError(
            f"\n🚱 There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"\n💧 Water left: Total water left after {days_left} days is: {total_water_left} liters"


try:
    print(water_left(3, 100, 2))
except RuntimeError as err:
    print(err)

try:
    print(water_left(6, 100, 2))
except RuntimeError as err:
    print(err)

try:
    print(water_left(6, 100, "hola"))
except TypeError as err:
    print(err)


# Ejercicio 2
print("\nEjercicio - Validar True o False:")
true_values = ['yes', 'y']
false_values = ['no', 'n']


def str_to_bool(value):
    value = value.lower()
    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError("Invalid entry")


try:
    print("Response:", str_to_bool("y"))
    print("Response:", str_to_bool("n"))
    print("Response:", str_to_bool("yes"))
    print("Response:", str_to_bool("Ninguna"))
except ValueError as err:
    print("Err:", err)
