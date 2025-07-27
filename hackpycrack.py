import os
import subprocess

def descifrar_hash(ruta_hash, ruta_diccionario):
    # Comando para descifrar el hash
    comando = f"hashcat -m 5600 --show '{ruta_hash}' '{ruta_diccionario}'"
    print(f"Ejecutando comando: {comando}")

    # Ejecutar el comando
    proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Recoger la salida del comando y decodificarla
    salida, _ = proceso.communicate()
    salida = salida.decode('utf-8')
    print("Salida del comando:")
    print(salida)

    # Buscar la línea que contiene el hash descifrado
    for linea in salida.split('\n'):
        print(f"Procesando línea: {linea}")
        if "FOUND" in linea:
            _, hash_descifrado = linea.split(':')
            usuario, contrasena = hash_descifrado.split(':')
            print(f"Usuario: {usuario}, Contraseña: {contrasena}")

# Rutas al archivo de hash y al diccionario
ruta_hash = "ruta absoluta del hash"
ruta_diccionario = "ruta absoluta del diccionario"

# Llamar a la función para descifrar el hash
descifrar_hash(ruta_hash, ruta_diccionario)
