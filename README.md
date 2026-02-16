# GUÍA RÁPIDA: Input y Guardado de Archivos en Python
## Para estudiantes de Python para VLSI

---

## USO DE INPUT()

### Básico
```python
# input() SIEMPRE devuelve un STRING
nombre = input("¿Tu nombre? ")
print(f"Hola, {nombre}")
```

### Convertir a Números
```python
# Para enteros
edad = int(input("¿Tu edad? "))

# Para decimales
voltaje = float(input("¿Voltaje? "))

# Científica (ejemplo: 10e-12)
capacitancia = float(input("¿Capacitancia en F? "))
```

### Con Validación (Recomendado)
```python
while True:
    try:
        R = float(input("Resistencia (Ω): "))
        if R > 0:  # Validar que sea positivo
            break
        print("Debe ser positivo")
    except ValueError:
        print("Número inválido, intente de nuevo")
```

---

##  GUARDAR ARCHIVOS

### Forma Básica (NO recomendada)
```python
# Abrir, escribir, cerrar manualmente
archivo = open('datos.txt', 'w')
archivo.write("Hola mundo\n")
archivo.close()  # ¡IMPORTANTE! No olvidar cerrar
```

### Forma Recomendada: usar WITH
```python
# Se cierra automáticamente al salir del bloque
with open('datos.txt', 'w') as archivo:
    archivo.write("Hola mundo\n")
    archivo.write("Segunda línea\n")
# Aquí el archivo ya está cerrado
```

---

##  MODOS DE APERTURA

| Modo | Nombre   | Descripción                          | Archivo debe existir |
|-------|------------|--------------------------------------|----------------------|
| `'r'` | Read       | Solo lectura                         |    Sí                |
| `'w'` | Write      | Escritura (BORRA contenido anterior) |    No (lo crea)      |
| `'a'` | Append     | Agrega al final (NO borra)           |    No (lo crea)      |
| `'r+'`| Read+Write | Lectura y escritura                  |    Sí                |

### Ejemplos
```python
# MODO 'w' - SOBRESCRIBE el archivo
with open('datos.txt', 'w') as f:
    f.write("Esto borra lo anterior\n")

# MODO 'a' - AGREGA al final
with open('log.txt', 'a') as f:
    f.write("Nueva línea al final\n")

# MODO 'r' - SOLO LECTURA
with open('datos.txt', 'r') as f:
    contenido = f.read()
    print(contenido)
```

---

##  ESCRIBIR EN ARCHIVOS

### Una línea a la vez
```python
with open('resultado.txt', 'w') as f:
    f.write("Primera línea\n")  # \n = salto de línea
    f.write("Segunda línea\n")
```

### Múltiples líneas de una vez
```python
lineas = [
    "Línea 1\n",
    "Línea 2\n",
    "Línea 3\n"
]

with open('resultado.txt', 'w') as f:
    f.writelines(lineas)
```

### Usando f-strings (MUY ÚTIL)
```python
delay = 125.3
power = 15.2

with open('reporte.txt', 'w') as f:
    f.write(f"Delay: {delay} ps\n")
    f.write(f"Power: {power} mW\n")
    f.write(f"Energía: {delay * power:.2f} pJ\n")
```

---

## LEER ARCHIVOS

### Leer todo el archivo de una vez
```python
with open('datos.txt', 'r') as f:
    contenido = f.read()  # String con todo el contenido
    print(contenido)
```

### Leer línea por línea (EFICIENTE para archivos grandes)
```python
with open('datos.txt', 'r') as f:
    for linea in f:
        print(linea.strip())  # .strip() quita \n
```

### Leer todas las líneas en una lista
```python
with open('datos.txt', 'r') as f:
    lineas = f.readlines()  # Lista de strings
    
for linea in lineas:
    print(linea.strip())
```

---

## GUARDAR EN FORMATO CSV

### Escribir CSV
```python
# Crear archivo CSV
with open('resultados.csv', 'w') as f:
    # Escribir encabezados
    f.write("simulacion,delay_ps,power_mw\n")
    
    # Escribir datos
    f.write(f"1,125.3,15.2\n")
    f.write(f"2,142.1,18.5\n")
    f.write(f"3,110.8,12.9\n")
```

### Agregar datos a CSV existente
```python
import os

csv_file = 'resultados.csv'

# Verificar si existe para escribir encabezado
if not os.path.exists(csv_file):
    with open(csv_file, 'w') as f:
        f.write("simulacion,delay_ps,power_mw\n")

# Agregar nueva fila
with open(csv_file, 'a') as f:
    f.write(f"4,135.7,16.8\n")
```

### Leer CSV manualmente
```python
with open('resultados.csv', 'r') as f:
    lineas = f.readlines()
    
    # Saltar encabezado
    for linea in lineas[1:]:
        datos = linea.strip().split(',')
        sim = datos[0]
        delay = float(datos[1])
        power = float(datos[2])
        print(f"Sim {sim}: {delay} ps, {power} mW")
```

---

## TÉCNICAS ÚTILES

### Verificar si archivo existe
```python
import os

if os.path.exists('archivo.txt'):
    print("El archivo existe")
else:
    print("El archivo NO existe")
```

### Obtener fecha/hora actual
```python
import datetime

ahora = datetime.datetime.now()
timestamp = ahora.strftime("%Y-%m-%d %H:%M:%S")

with open('log.txt', 'a') as f:
    f.write(f"{timestamp} - Simulación completada\n")
```

### Nombres de archivo dinámicos
```python
simulacion_num = 5
filename = f"sim_{simulacion_num:03d}.txt"  # sim_005.txt

with open(filename, 'w') as f:
    f.write("Resultados de simulación\n")
```

---

## EJEMPLO COMPLETO: Registro de Simulaciones

```python
import os
import datetime

# Solicitar datos al usuario
sim_num = int(input("Número de simulación: "))
delay = float(input("Delay (ps): "))
power = float(input("Power (mW): "))

# Timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Archivo CSV para datos
csv_file = 'simulaciones.csv'

# Crear encabezado si no existe
if not os.path.exists(csv_file):
    with open(csv_file, 'w') as f:
        f.write("timestamp,simulacion,delay_ps,power_mw\n")

# Agregar datos
with open(csv_file, 'a') as f:
    f.write(f"{timestamp},{sim_num},{delay},{power}\n")

# Archivo de log legible
with open('simulaciones_log.txt', 'a') as f:
    f.write(f"[{timestamp}] Sim #{sim_num:03d}: ")
    f.write(f"Delay={delay:.2f}ps, Power={power:.2f}mW\n")

# Reporte individual
with open(f'sim_{sim_num:03d}_report.txt', 'w') as f:
    f.write("="*50 + "\n")
    f.write(f"REPORTE DE SIMULACIÓN #{sim_num}\n")
    f.write("="*50 + "\n\n")
    f.write(f"Fecha:     {timestamp}\n")
    f.write(f"Delay:     {delay} ps\n")
    f.write(f"Power:     {power} mW\n")
    f.write(f"Energía:   {delay * power:.2f} pJ\n")
    f.write("="*50 + "\n")

print(f"\n✓ Datos guardados en:")
print(f"  {csv_file}")
print(f"  simulaciones_log.txt")
print(f"  sim_{sim_num:03d}_report.txt")
```

---

## ERRORES COMUNES

### 1. Olvidar cerrar archivo
```python
# MAL (sin cerrar)
f = open('datos.txt', 'w')
f.write("Hola")
# ¡Falta f.close()!

# BIEN (con 'with')
with open('datos.txt', 'w') as f:
    f.write("Hola")
# Se cierra automáticamente
```

### 2. No agregar \n al final de líneas
```python
# MAL (todo en una línea)
with open('datos.txt', 'w') as f:
    f.write("Línea 1")
    f.write("Línea 2")
# Resultado: "Línea 1Línea 2"

# BIEN
with open('datos.txt', 'w') as f:
    f.write("Línea 1\n")
    f.write("Línea 2\n")
# Resultado:
# Línea 1
# Línea 2
```

### 3. Usar 'w' cuando se quiere 'a'
```python
# MAL - Borra datos anteriores
for i in range(5):
    with open('log.txt', 'w') as f:  # ¡'w' borra!
        f.write(f"Iteración {i}\n")
# Solo queda la última iteración

# BIEN - Acumula datos
for i in range(5):
    with open('log.txt', 'a') as f:  # 'a' agrega
        f.write(f"Iteración {i}\n")
# Quedan las 5 iteraciones
```

### 4. No validar entrada del usuario
```python
# MAL (sin validación)
R = float(input("Resistencia: "))  # ¿Y si escriben "abc"?

# BIEN
while True:
    try:
        R = float(input("Resistencia: "))
        if R > 0:
            break
        print("Debe ser positiva")
    except ValueError:
        print("Número inválido")
```

---

## PARA RECORDAR

1. **`input()` SIEMPRE devuelve string** → convertir con `int()` o `float()`

2. **Usar `with open()` siempre** → cierra automáticamente

3. **Modos:**
   - `'w'` = borra todo y escribe
   - `'a'` = agrega al final
   - `'r'` = solo lectura

4. **Agregar `\n` para nuevas líneas**

5. **Validar entradas del usuario** con try-except

6. **Verificar existencia** con `os.path.exists()`

---

## EJERCICIO PROPUESTO

Cree un programa que:
1. Solicite: nombre del módulo, delay, potencia, área
2. Guarde en CSV acumulativo
3. Guarde reporte individual en .txt
4. Al final, muestre estadísticas de TODOS los módulos guardados

---

**¡Consulta los ejemplos completos para más detalles!**
- `ejemplo1_basico_input_archivos.py`
- `ejemplo2_vlsi_netlist_generator.py`
- `ejemplo3_tecnicas_avanzadas_archivos.py`
