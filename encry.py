from cryptography.fernet import Fernet
import re
import os
from os import system

archivo = open("passw.txt","r")
plain_txt = str(archivo.read())
archivo.close()

clave = re.search(r"(^.*)\n",plain_txt).group(0)
mensaje = re.search(r"\n(.*)\n",plain_txt).group(0)
f = Fernet(clave)
dessen = f.decrypt(mensaje)

archivo = open("pass_plain.txt","w+")
archivo.write(dessen.decode())
archivo.close()

print("OK - Mostrando los datos desencriptados")
system('.\pass_plain.txt')
print("Datos cifrados ........................")

archivo = open("pass_plain.txt","r")
plain_txt = str(archivo.read())
archivo.close()

claveNueva = Fernet.generate_key()
f = Fernet(claveNueva)

encriptado = f.encrypt(plain_txt.encode())
archivo = open("passw.txt","w+")
archivo.write(claveNueva.decode()+"\n")
archivo.write(encriptado.decode()+"\n")
archivo.close()

if "pass_plain.txt" in os.listdir():
    os.remove("pass_plain.txt")