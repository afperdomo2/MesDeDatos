import sys

"1" + 2
# Recopilación de entradas

# 1. Entrada de la línea de comandos

# Ejecutar el siguiente comando en consola. Realiza la entrada
# de 2 argumentos. La fecha y el string de `saludar`

# python EntradaDatos.py 2023-01-01 Saludar

print("Todos argumentos:", sys.argv)
print("Nombre del programa:", sys.argv[0])
print("Argumento 1:", sys.argv[1])
print("Argumento 2:", sys.argv[2])


# 2. Entrada de usuario
print("\n🖖 Programa de Bienvenida")
name = input("➡️  Ingrese su nombre: ")
print("Saludos " + name)


print("\n📈 Calculadora")
first_number = input("➡️  Primer número: ")
second_number = input("➡️  Segundo número: ")
sum = int(first_number) + int(second_number)
print("La suma es:", sum)
