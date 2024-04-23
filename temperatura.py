# Definir una función para definir Fahrenheit a Celsius
def fahrenheit_a_celsius(temperatura):
    return (temperatura - 32) / 1.8


celsius = fahrenheit_a_celsius(17)
print(f'La temperatura en celsius es: {celsius}')

celsius = fahrenheit_a_celsius(41)
print(f'La temperatura en celsius es: {celsius}')