# BINARY SNAKE

## Integrantes
* Alejandro Cáceres [202373520-5] (Paralelo 200)
* Miguel Salamanca [202373564-7] (Paralelo 200)

## Descripcion

Generación del tablero: Se crea una matriz largo x 11 con la serpiente (S), guardias (!), objetivo (*) y casillas vacías (X). Las posiciones de guardias y objetivo se generan aleatoriamente.

Conversión de bases: El jugador ingresa distancias en binario, octal o hexadecimal, según el tamaño del tablero. Los algoritmos calcularBase y calcularDecimal realizan las conversiones necesarias.

Movimiento de la serpiente: La serpiente se mueve en pasos verificando si alcanza el objetivo (gana), choca con un guardia (pierde) o continúa.

Lógica de hackeo: Al llegar al objetivo, el jugador debe convertir correctamente un número de la base del tablero a decimal para ganar.
Para ejecutar el codigo, usar el comando:
```
python t1.py
```
ó
```
python3 t1.py
```

## Requerimientos
* Python 3.X
    - Utilizado y recomendado [Python 3.13.0](https://www.python.org/downloads/release/python-3130/)
