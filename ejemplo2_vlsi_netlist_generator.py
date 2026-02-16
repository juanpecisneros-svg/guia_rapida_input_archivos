#!/usr/bin/env python3
"""
EJEMPLO 2: Aplicación VLSI - Generador de Netlist SPICE
========================================================

Este ejemplo muestra cómo usar input() y guardado de archivos
en un contexto real de diseño VLSI.

Objetivo: Crear un netlist SPICE simple pidiendo datos al usuario

Autor: Preparado para estudiantes de Python para VLSI
Nivel: Principiante-Intermedio
"""

print("="*70)
print("  GENERADOR DE NETLIST SPICE - Circuito RC Simple")
print("="*70)

# ============================================================================
# PASO 1: SOLICITAR INFORMACIÓN AL USUARIO
# ============================================================================

print("\nIngrese los parámetros del circuito RC:")
print("-"*70)

# Solicitar valores con validación básica
while True:
    try:
        # Solicitar resistencia
        R_str = input("Resistencia (en Ohms, ej: 1000): ")
        R = float(R_str)  # Convertir a número decimal
        
        if R <= 0:
            print("    Error: La resistencia debe ser positiva")
            continue
        break
    except ValueError:
        print("    Error: Ingrese un número válido")

while True:
    try:
        # Solicitar capacitancia
        C_str = input("Capacitancia (en Farads, ej: 10e-12 para 10pF): ")
        C = float(C_str)
        
        if C <= 0:
            print("    Error: La capacitancia debe ser positiva")
            continue
        break
    except ValueError:
        print("    Error: Ingrese un número válido")

# Voltaje de alimentación
V_supply = float(input("Voltaje de alimentación (en Volts, ej: 1.8): "))

# Nombre del circuito
circuit_name = input("Nombre del circuito (ej: rc_filter): ")

# Validar que el nombre sea válido (sin espacios)
circuit_name = circuit_name.replace(" ", "_")  # Reemplazar espacios por _


# ============================================================================
# PASO 2: CALCULAR PARÁMETROS DERIVADOS
# ============================================================================

import math

tau = R * C  # Constante de tiempo
fc = 1 / (2 * math.pi * tau)  # Frecuencia de corte

print("\n" + "-"*70)
print("Parámetros calculados:")
print(f"  τ (tau)     = {tau:.3e} segundos")
print(f"  fc (cutoff) = {fc:.3e} Hz")
print("-"*70)


# ============================================================================
# PASO 3: GENERAR EL NETLIST SPICE
# ============================================================================

# Construir el contenido del netlist
netlist_content = f"""* Netlist SPICE - Circuito RC
* Generado automáticamente por Python
* Circuito: {circuit_name}
* Fecha: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

* ============================================================
* PARÁMETROS DEL CIRCUITO
* ============================================================
* Resistencia:    {R} Ohms
* Capacitancia:   {C:.3e} F
* Voltaje:        {V_supply} V
* Tau:            {tau:.3e} s
* Freq. corte:    {fc:.3e} Hz
* ============================================================

* Fuente de voltaje
V1 vdd 0 DC {V_supply}V

* Componentes pasivos
R1 vdd node1 {R}
C1 node1 0 {C:.3e}F

* Análisis transitorio
.tran 1ps {tau*10:.3e}s

* Control
.control
run
plot v(node1)
.endc

.end
"""

# ============================================================================
# PASO 4: GUARDAR EL NETLIST EN UN ARCHIVO
# ============================================================================

# Nombre del archivo
filename = f"{circuit_name}.sp"

# Guardar usando 'with' (forma recomendada)
with open(filename, 'w') as file:
    file.write(netlist_content)

print(f"\n Netlist guardado en: {filename}")


# ============================================================================
# PASO 5: TAMBIÉN GUARDAR UN REPORTE RESUMIDO
# ============================================================================

# Crear un reporte en formato más legible
report_content = f"""REPORTE DEL CIRCUITO RC
{'='*70}

PARÁMETROS DE ENTRADA:
  • Resistencia (R):     {R:>15} Ω
  • Capacitancia (C):    {C:>15.3e} F
  • Voltaje (Vdd):       {V_supply:>15} V

PARÁMETROS CALCULADOS:
  • Constante de tiempo (τ):  {tau:>15.3e} s
  • Frecuencia de corte (fc): {fc:>15.3e} Hz
  • Periodo (T):              {1/fc:>15.3e} s

ARCHIVOS GENERADOS:
  • Netlist SPICE: {filename}
  • Este reporte:  {circuit_name}_report.txt

{'='*70}
Generado con Python para VLSI
"""

# Guardar el reporte
report_filename = f"{circuit_name}_report.txt"
with open(report_filename, 'w') as file:
    file.write(report_content)

print(f" Reporte guardado en: {report_filename}")


# ============================================================================
# PASO 6: MOSTRAR VISTA PREVIA DE LOS ARCHIVOS
# ============================================================================

print("\n" + "="*70)
print("VISTA PREVIA DEL NETLIST SPICE:")
print("="*70)
print(netlist_content)

print("\n" + "="*70)
print("VISTA PREVIA DEL REPORTE:")
print("="*70)
print(report_content)


# ============================================================================
# BONUS: PREGUNTAR SI DESEA GENERAR OTRO CIRCUITO
# ============================================================================

print("\n" + "="*70)
respuesta = input("¿Desea generar otro circuito? (s/n): ")

if respuesta.lower() == 's' or respuesta.lower() == 'si':
    print("\nPara generar otro circuito, ejecute el programa nuevamente.")
else:
    print("\n¡Gracias por usar el generador de netlists!")

print("\nFin del programa.\n")


# ============================================================================
# CONCEPTOS CLAVE DEMOSTRADOS:
# ============================================================================
"""
1. INPUT CON VALIDACIÓN:
   - Uso de try-except para manejar errores
   - Bucle while para repetir hasta obtener entrada válida
   - Conversión de strings a números (int, float)

2. MANIPULACIÓN DE STRINGS:
   - f-strings para formateo
   - .replace() para limpiar nombres
   - Formato de números con :.3e (notación científica)

3. GUARDADO DE ARCHIVOS:
   - Uso de 'with' para abrir archivos
   - Modo 'w' para escritura
   - Escribir strings con .write()

4. BUENAS PRÁCTICAS:
   - Nombres de archivo dinámicos
   - Comentarios extensivos en el código
   - Validación de entradas del usuario
   - Mensajes informativos al usuario
"""
