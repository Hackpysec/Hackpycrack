# Hackpycrack
Hackpycrack es una herramienta de descifrado de hashes que utiliza hashcat y Python para descifrar hashes NTLMv2.

<br/>

## Dependencias

Para ejecutar Hackpycrack, necesitarás tener instalado lo siguiente en tu sistema:

- Python 3
- hashcat

<br/>

## Instalación

Para instalar las dependencias en Ubuntu, puedes usar los siguientes comandos:

```bash
sudo apt update
sudo apt install python3
sudo apt install hashcat
```

<br/>

## Uso
Para usar Hackpycrack, necesitarás tener un archivo de hash y un diccionario. Luego, puedes ejecutar el script de la siguiente manera:

```bash
python3 hackpycrack.py
```

<br/>

## Ejemplo
Aquí tienes un ejemplo de cómo usar Hackpycrack:

```bash
python3 hackpycrack.py /ruta/a/tu/archivo/hash /ruta/a/tu/diccionario
```

Este comando intentará descifrar el hash en el archivo especificado utilizando el diccionario proporcionado.
