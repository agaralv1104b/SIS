# Calculadora binaria de 8 bits (Python) — README

> Calculadora que suma y resta números binarios de 1 a 8 bits.
>
> Los operandos se rellenan con ceros a la izquierda hasta alcanzar los 8 bits.
>
> Si no se indica ningún signo, el programa ejecuta ambas operaciones.

---

## 1) Descripción del módulo

Este proyecto implementa una calculadora binaria de 8 bits que permite realizar sumas y restas entre dos operandos.

- Los operandos se introducen mediante `input()` como cadenas de entre 1 y 8 bits.
- Solo se admiten los caracteres `0` y `1`.
- La operación se introduce mediante `input()`: `+` para sumar o `-` para restar.
- Si se deja la operación vacía, se realizan ambas operaciones.
- Los operandos se rellenan con ceros a la izquierda mediante `zfill(8)`.
- Las operaciones se realizan bit a bit utilizando bucles y variables de acarreo.
- Si una suma genera un acarreo adicional, el resultado tendrá 9 bits.
- Si el segundo operando es mayor que el primero al realizar una resta, se muestra el mensaje `Resta negativa`.
- Contiene comentarios para guiarme y tenerlo de modo apuntes tambien.

---

## 2) Requisitos

- Python 3.
- No necesita dependencias externas.

---

## 3) Instalación de Python

### 3.1 Linux

#### Debian/Ubuntu y derivados

```bash
sudo apt update
sudo apt install -y python3
python3 --version
```

### 3.2 Windows

Se puede descargar Python desde su página oficial:

https://www.python.org/downloads/

Durante la instalación, es recomendable marcar la opción `Add Python to PATH`.

Para comprobar la instalación, ejecuta en una terminal:

```powershell
py --version
```

---

## 4) Ejecución del módulo

Para ejecutar el programa, abre una terminal en la carpeta donde se encuentra el archivo `nuevasuma.py` y ejecuta:

```bash
python3 nuevasuma.py
```

En Windows puedes utilizar:

```powershell
py nuevasuma.py
```

Al iniciar el programa, se solicitan los siguientes datos:

1. Primer operando binario.
2. Operación: `+`, `-` o dejar el campo vacío.
3. Segundo operando binario.

### Ejemplos

**Suma**

Entrada:

```text
Ingrese el primer operando: 101
+ / -: +
Ingrese el segundo operando: 11
```

Salida:

```text
00001000
```

**Resta**

Entrada:

```text
Ingrese el primer operando: 1100
+ / -: -
Ingrese el segundo operando: 101
```

Salida:

```text
00000111
```

**Sin signo: realiza ambas operaciones**

Entrada:

```text
Ingrese el primer operando: 1100
+ / -:
Ingrese el segundo operando: 101
```

Salida:

```text
00010001
00000111
```

La primera línea corresponde a la suma y la segunda a la resta.

---

## 5) Dependencias con `dependencias.txt` (opcional)

El programa no necesita dependencias externas, por lo que no es necesario crear un archivo `dependencias.txt`.

---

## 6) Mensajes de error y códigos de salida

El programa realiza varias comprobaciones para evitar entradas incorrectas.

- **Operandos vacíos:** muestra `ERROR: los operando no pueden estar vacios...`.
- **Operandos de más de 8 bits:** muestra `ERROR: los operando no pueden contener mas de 8 bits`.
- **Caracteres no binarios:** muestra `ERROR: solo se aceptaran 0 y 1`.
- **Operación no válida:** muestra `ERROR: la operacion solo admite +/-`.
- **Resta negativa:** muestra `Resta negativa` cuando el segundo operando es mayor que el primero.

Cuando se detecta uno de estos errores, el programa utiliza `exit()` para finalizar la ejecución.

---