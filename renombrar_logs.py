from pathlib import Path

# Carpeta donde se encuentran los archivos de logs
carpeta_logs = Path("logs")

# Nombre base solicitado para los archivos
nombre_base = "rene_merino"

# Validar que la carpeta exista
if not carpeta_logs.exists():
    print("La carpeta 'logs' no existe. Debe crearla antes de ejecutar el script.")
    exit()

# Filtrar solo archivos con extensión .log
archivos_log = sorted(carpeta_logs.glob("*.log"))

# Validar si existen archivos .log
if not archivos_log:
    print("No se encontraron archivos .log para renombrar.")
    exit()

print("Archivos .log encontrados:")
for archivo in archivos_log:
    print(f"- {archivo.name}")

# Primera etapa: renombrar temporalmente para evitar conflictos de nombres
archivos_temporales = []

for numero, archivo in enumerate(archivos_log, start=1):
    archivo_temporal = carpeta_logs / f"temporal_{numero}.tmp"
    archivo.rename(archivo_temporal)
    archivos_temporales.append(archivo_temporal)

# Segunda etapa: renombrar con el formato final solicitado
print("\nRenombrando archivos:")

for numero, archivo_temporal in enumerate(archivos_temporales, start=1):
    nuevo_nombre = carpeta_logs / f"{nombre_base}_{numero}.log"
    archivo_temporal.rename(nuevo_nombre)
    print(f"{archivo_temporal.name} -> {nuevo_nombre.name}")

print("\nProceso finalizado correctamente.")