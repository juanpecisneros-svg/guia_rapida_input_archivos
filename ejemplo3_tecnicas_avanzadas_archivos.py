#!/usr/bin/env python3
"""
EJEMPLO 3: Técnicas Avanzadas de Input y Guardado de Archivos
===============================================================

Este ejemplo muestra diferentes formas de trabajar con archivos:
1. Modo append (agregar al final)
2. Guardado de CSV
3. Guardado de múltiples formatos

Aplicación: Registro de resultados de simulación

Autor: Preparado para estudiantes de Python para VLSI
Nivel: Intermedio
"""

import datetime  # Para obtener fecha/hora actual

print("="*70)
print("  REGISTRO DE RESULTADOS DE SIMULACIÓN")
print("="*70)


# ============================================================================
# FUNCIÓN AUXILIAR: Solicitar número con validación
# ============================================================================

def solicitar_numero(mensaje, tipo=float):
    """
    Solicita un número al usuario con validación
    
    Args:
        mensaje: Texto a mostrar al usuario
        tipo: int o float (tipo de número esperado)
    
    Returns:
        Número validado del tipo especificado
    """
    while True:
        try:
            valor_str = input(mensaje)
            valor = tipo(valor_str)
            return valor
        except ValueError:
            print(f"    Error: Ingrese un número válido")


# ============================================================================
# EJEMPLO 1: MODO APPEND - Agregar datos sin borrar lo anterior
# ============================================================================

print("\n" + "-"*70)
print("EJEMPLO 1: Modo APPEND - Registro acumulativo")
print("-"*70)

print("\nIngrese los resultados de la simulación:")

# Solicitar datos
simulacion_num = solicitar_numero("Número de simulación: ", int)
delay_ps = solicitar_numero("Delay (ps): ", float)
power_mw = solicitar_numero("Potencia (mW): ", float)

# Obtener timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# MODO 'a' = APPEND
# Si el archivo existe, agrega al final
# Si no existe, lo crea
log_filename = "simulaciones_log.txt"

with open(log_filename, 'a') as archivo:  # 'a' = append
    # Formato: timestamp | simulacion | delay | power
    linea = f"{timestamp} | Sim #{simulacion_num:03d} | Delay: {delay_ps:6.2f} ps | Power: {power_mw:5.2f} mW\n"
    archivo.write(linea)

print(f"\n Resultado agregado a '{log_filename}'")
print(f"  Ejecute el programa varias veces y verá cómo se acumulan los datos")


# ============================================================================
# EJEMPLO 2: GUARDAR EN FORMATO CSV
# ============================================================================

print("\n" + "-"*70)
print("EJEMPLO 2: Formato CSV (Comma-Separated Values)")
print("-"*70)

print("\nEl mismo dato se guardará también en formato CSV")
print("(Ideal para abrir en Excel o procesar con Pandas)")

csv_filename = "simulaciones_resultados.csv"

# Verificar si el archivo existe
import os
archivo_existe = os.path.exists(csv_filename)

with open(csv_filename, 'a') as archivo:
    # Si el archivo no existe, escribir encabezados
    if not archivo_existe:
        encabezado = "timestamp,simulacion,delay_ps,power_mw\n"
        archivo.write(encabezado)
    
    # Escribir los datos (sin espacios, separados por comas)
    linea_csv = f"{timestamp},{simulacion_num},{delay_ps},{power_mw}\n"
    archivo.write(linea_csv)

print(f" Resultado guardado en '{csv_filename}'")


# ============================================================================
# EJEMPLO 3: FORMATO ESTRUCTURADO (para análisis posterior)
# ============================================================================

print("\n" + "-"*70)
print("EJEMPLO 3: Archivo estructurado con formato fijo")
print("-"*70)

# Solicitar información adicional
esquina = input("Esquina de simulación (TT/SS/FF): ").upper()
temperatura = solicitar_numero("Temperatura (°C): ", int)

# Crear un reporte estructurado
reporte_filename = f"sim_{simulacion_num:03d}_report.txt"

with open(reporte_filename, 'w') as archivo:
    # Escribir línea por línea con formato
    archivo.write("="*70 + "\n")
    archivo.write("REPORTE DE SIMULACIÓN\n")
    archivo.write("="*70 + "\n\n")
    
    archivo.write(f"Número de simulación:  {simulacion_num:03d}\n")
    archivo.write(f"Fecha y hora:          {timestamp}\n")
    archivo.write(f"Esquina de proceso:    {esquina}\n")
    archivo.write(f"Temperatura:           {temperatura}°C\n\n")
    
    archivo.write("-"*70 + "\n")
    archivo.write("RESULTADOS\n")
    archivo.write("-"*70 + "\n\n")
    
    archivo.write(f"Delay:     {delay_ps:>10.2f} ps\n")
    archivo.write(f"Potencia:  {power_mw:>10.2f} mW\n\n")
    
    archivo.write("="*70 + "\n")
    archivo.write("Fin del reporte\n")

print(f" Reporte individual guardado en '{reporte_filename}'")


# ============================================================================
# EJEMPLO 4: LEER Y MOSTRAR TODO EL LOG
# ============================================================================

print("\n" + "-"*70)
print("EJEMPLO 4: Lectura del log acumulado")
print("-"*70)

print(f"\nContenido completo de '{log_filename}':")
print("-"*70)

# Verificar que el archivo existe antes de leer
if os.path.exists(log_filename):
    with open(log_filename, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
else:
    print("(El archivo aún no existe)")


# ============================================================================
# EJEMPLO 5: LEER CSV Y PROCESAR DATOS
# ============================================================================

print("\n" + "-"*70)
print("EJEMPLO 5: Lectura y análisis del CSV")
print("-"*70)

if os.path.exists(csv_filename):
    print(f"\nDatos del archivo '{csv_filename}':")
    print("-"*70)
    
    with open(csv_filename, 'r') as archivo:
        # Leer línea por línea
        lineas = archivo.readlines()
        
        # La primera línea son los encabezados
        print(lineas[0].strip())  # Imprimir encabezados
        print("-"*70)
        
        # Procesar las líneas de datos
        total_delay = 0
        total_power = 0
        num_simulaciones = 0
        
        for linea in lineas[1:]:  # Saltar encabezado
            # Separar por comas
            datos = linea.strip().split(',')
            
            # Extraer valores
            timestamp_csv = datos[0]
            sim_num = datos[1]
            delay = float(datos[2])
            power = float(datos[3])
            
            # Imprimir
            print(f"{timestamp_csv} | Sim #{sim_num} | {delay:.2f} ps | {power:.2f} mW")
            
            # Acumular para estadísticas
            total_delay += delay
            total_power += power
            num_simulaciones += 1
        
        # Mostrar estadísticas
        if num_simulaciones > 0:
            print("\n" + "="*70)
            print("ESTADÍSTICAS:")
            print(f"  Total de simulaciones: {num_simulaciones}")
            print(f"  Delay promedio:        {total_delay/num_simulaciones:.2f} ps")
            print(f"  Potencia promedio:     {total_power/num_simulaciones:.2f} mW")
            print("="*70)
else:
    print("(El archivo CSV aún no existe)")


# ============================================================================
# RESUMEN Y DOCUMENTACIÓN
# ============================================================================

print("\n\n" + "="*70)
print("RESUMEN DE CONCEPTOS")
print("="*70)

print("""
1. MODOS DE APERTURA DE ARCHIVOS:
   'r'  - Lectura (read)       - Archivo debe existir
   'w'  - Escritura (write)    - BORRA contenido anterior
   'a'  - Agregar (append)     - Agrega al final, NO borra
   'r+' - Lectura + escritura  - Archivo debe existir

2. VERIFICAR SI ARCHIVO EXISTE:
   import os
   if os.path.exists('archivo.txt'):
       # hacer algo

3. FORMATO CSV:
   - Valores separados por comas
   - Primera línea = encabezados
   - Fácil de leer con Excel o Pandas

4. BUENAS PRÁCTICAS:
   - Usar 'with' para abrir archivos (cierre automático)
   - Validar entradas del usuario
   - Agregar timestamps a los logs
   - Usar nombres de archivo descriptivos

5. ARCHIVOS CREADOS POR ESTE PROGRAMA:
   • simulaciones_log.txt          (log acumulativo)
   • simulaciones_resultados.csv   (datos en formato CSV)
   • sim_XXX_report.txt            (reporte individual)
""")

print("="*70)
print("\n Programa completado")
print("  Ejecute este script varias veces para ver cómo se acumulan los datos\n")


# ============================================================================
# EJERCICIO PARA EL ESTUDIANTE:
# ============================================================================
"""
EJERCICIO PROPUESTO:
-------------------
Modifique este programa para que:

1. Solicite también el voltaje (VDD) de la simulación

2. Calcule y guarde la energía (E = Power x Delay)

3. Agregue una opción al final que pregunte:
   "¿Desea ver el resumen de todas las simulaciones? (s/n)"
   
   Si el usuario dice 's', mostrar:
   - Número total de simulaciones
   - Delay máximo, mínimo y promedio
   - Potencia máxima, mínima y promedio
   - Energía total consumida

4. BONUS: Guardar el resumen en un archivo llamado
   'resumen_simulaciones.txt' cada vez que se genera

PISTA: Necesitarás leer el archivo CSV, procesar todos los datos
       y calcular las estadísticas.
"""
