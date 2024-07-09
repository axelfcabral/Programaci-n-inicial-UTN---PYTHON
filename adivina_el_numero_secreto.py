secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, Junior!|
| Introduce un número entero |
| y adivina qué número he |
| elegido para ti. |
|¿Cuál es el número secreto? |
+================================+
""")

number = int(input('El numero secreto es: '))

while number  != 777: 
    print('¡Ja, ja! ¡Estás atrapado en mi bucle!')
    number = int(input('El numero secreto es: '))

print('¡Bien hecho, Junior! Eres libre ahora.' )
