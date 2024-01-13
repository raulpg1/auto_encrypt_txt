# Script para guardar datos encriptados en un archivo txt.
### Contenido:
  -  passwd.txt -> archivo que contiene los datos encriptados y la clave para desencriptarlos
  -  encry.py -> script
    
### Modo de ejecución:
  -  Se ejecuta el archivo .bat que lanza el script
  -  Al ejecutar, se lee la primera linea del archivo passw.txt que tiene la clave de encriptado
  -  Se desenccriptan los datos y se genera un nuevo txt temporal con los datos
  -  Este txt también se puede editar y sus datos se encriptan con una nueva clave
  -  Al cerrar el txt, los datos se vuelven a encriptar con una nueva clave generada
