# SCANN IPs To URLs In Python.
# by Root - @anonymousCRI...

import socket
import pyfiglet

banner = pyfiglet.figlet_format("Skyhawk - Rootr | MortenTod", font="small")

lines = banner.split("\n")
lines[-2] += "    @anonymousCRI"
banner_mod = "\n".join(lines)


print(banner_mod)

print("Skyhawk:")
print("Una herramienta de Pentesting diseñada en Python para escanear Protocolos de Internet (IP) a URLs mediante su Dominio.")
print("                                                    ")

my_url = input("Escriba su Dominio aquí: ",)
my_ip = socket.gethostbyname(my_url)
print("La dirección IP de su Dominio es:", "\033[92m" + my_ip + "\033[0m")