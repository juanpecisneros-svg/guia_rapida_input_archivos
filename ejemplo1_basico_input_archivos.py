#!/usr/bin/env python3
"""
EJEMPLO 1: Lo más básico - Input y Guardado de Archivos
=========================================================

Este ejemplo muestra los conceptos fundamentales de:
1. Obtener información del usuario con input()
2. Guardar información en un archivo de texto

Autor: Preparado para estudiantes de Python para VLSI
Nivel: Principiante
"""

# ============================================================================
# PARTE 1: USO BÁSICO DE INPUT()
# ============================================================================

print("="*60)
print("  EJEMPLO BÁSICO: INPUT Y ARCHIVOS")
print("="*60)

# input() siempre devuelve un STRING (texto)
# Por eso necesitamos convertir si queremos números

# Solicitar nombre del usuario
nombre = input("\n¿Cuál es tu nombre? ")
print(f"Hola, {nombre}!")

# Solicitar un número (necesitamos convertir a int)
edad = input("¿Cuántos años tienes? ")
edad = int(edad)  # Convertir string a entero
print(f"Tienes {edad} años.")

# Forma más corta: convertir en la misma línea
altura = int(input("¿Cuál es tu altura en cm? "))
print(f"Tu altura es {altura} cm.")


# ============================================================================
# PARTE 2: GUARDAR EN UN ARCHIVO DE TEXTO
# ============================================================================

print("\n" + "-"*60)
print("Ahora vamos a guardar esta información en un archivo...")
print("-"*60)

# Forma 1: Abrir, escribir y cerrar manualmente
archivo = open('datos_usuario.txt', 'w')  # 'w' = write (escritura)
archivo.write(f"Nombre: {nombre}\n")
archivo.write(f"Edad: {edad}\n")
archivo.write(f"Altura: {altura} cm\n")
archivo.close()  # ¡IMPORTANTE! Siempre cerrar el archivo

print(" Archivo 'datos_usuario.txt' creado")


# Forma 2: Usar 'with' (RECOMENDADO - cierra automáticamente)
with open('datos_usuario_v2.txt', 'w') as archivo:
    archivo.write(f"Nombre: {nombre}\n")
    archivo.write(f"Edad: {edad}\n")
    archivo.write(f"Altura: {altura} cm\n")
    # Al salir del bloque 'with', el archivo se cierra automáticamente

print(" Archivo 'datos_usuario_v2.txt' creado")


# Forma 3: Escribir múltiples líneas a la vez
lineas = [
    f"Nombre: {nombre}\n",
    f"Edad: {edad}\n",
    f"Altura: {altura} cm\n"
]

with open('datos_usuario_v3.txt', 'w') as archivo:
    archivo.writelines(lineas)  # Escribe todas las líneas

print(" Archivo 'datos_usuario_v3.txt' creado")


# ============================================================================
# PARTE 3: LEER EL ARCHIVO QUE GUARDAMOS
# ============================================================================

print("\n" + "-"*60)
print("Leyendo el archivo que guardamos...")
print("-"*60)

# Leer todo el archivo de una vez
with open('datos_usuario.txt', 'r') as archivo:  # 'r' = read (lectura)
    contenido = archivo.read()
    print(contenido)

# Leer línea por línea
print("\nLeyendo línea por línea:")
with open('datos_usuario.txt', 'r') as archivo:
    for linea in archivo:
        print(f"  > {linea.strip()}")  # .strip() quita el salto de línea


# ============================================================================
# RESUMEN DE MODOS DE APERTURA
# ============================================================================

print("\n" + "="*60)
print("RESUMEN: Modos de apertura de archivos")
print("="*60)
print("'r'  - Lectura (read)        - El archivo debe existir")
print("'w'  - Escritura (write)     - Sobrescribe si existe")
print("'a'  - Añadir (append)       - Agrega al final del archivo")
print("'r+' - Lectura y escritura   - El archivo debe existir")
print("="*60)

print("\n¡Ejemplo completado!")
print("Revisa los archivos .txt que se crearon en este directorio.\n")
