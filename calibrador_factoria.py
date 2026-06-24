import time

# --- 1. Variables (Contenedores de memoria como en tu bitácora) ---
nombre_proyecto = "Mi Primer Repositorio"
ancho_carril_pistas = 80  # Calibración base en píxeles
estado_maquina = "LISTO"

print(f"--- Iniciando Script: {nombre_proyecto} ---")
print(f"Calibración actual del carril: {ancho_carril_pistas}px")
time.sleep(1)  # Control de ritmo: pausa de 1 segundo

# --- 2. Tubería de Condicionales (Toma de decisiones estricta) ---
# Simulamos una prueba de teclado o ingreso de comando
comando_usuario = "FLECHA_DERECHA"  

if comando_usuario == "FLECHA_IZQUIERDA":
    print("Moviendo estructura a la izquierda... Ajustando milímetros.")
elif comando_usuario == "FLECHA_DERECHA":
    # Modificamos la variable intencionalmente para probar límites
    ancho_carril_pistas = 90  
    print(f"¡Límite alterado! Nuevo ancho de carril: {ancho_carril_pistas}px")
    print("La matemática fría y proporcional responde correctamente.")
else:
    print("Comando inválido. El sistema no reacciona por descarte masivo.")

time.sleep(1)
print("\n--- Máxima del Inventor ---")
print('"Si le metes un plano bien diseñado, te construye un imperio."')
