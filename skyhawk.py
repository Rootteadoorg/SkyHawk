# SCANN IPs To URLs In Python.
# by Root - @anonymousCRI...

import socket
import os
import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.02, color=Fore.GREEN):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print()

def efecto(texto, ciclos=12, delay=0.5):
    texto = Fore.GREEN + texto
    for i in range(ciclos):
        puntos = "." * (i % 4)
        sys.stdout.write("\r" + texto + puntos + "   ")
        sys.stdout.flush()
        time.sleep(delay)
    print()


def hawk_banner():
    clear()
    print(Fore.CYAN + Style.BRIGHT + r"""
                ███████╗██╗  ██╗██╗   ██╗██╗  ██╗ █████╗ ██╗    ██╗██╗  ██╗
                ██╔════╝██║ ██╔╝╚██╗ ██╔╝██║  ██║██╔══██╗██║    ██║██║ ██╔╝
                ███████╗█████╔╝  ╚████╔╝ ███████║███████║██║ █╗ ██║█████╔╝ 
                ╚════██║██╔═██╗   ╚██╔╝  ██╔══██║██╔══██║██║███╗██║██╔═██╗ 
                ███████║██║  ██╗   ██║   ██║  ██║██║  ██║╚███╔███╔╝██║  ██╗
                ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝

                            ── @anonymousCRI ──
                            "Ojos en el cielo."
    """)

    print(Fore.GREEN + "  | Tool: Una herramienta de Pentesting diseñada en Python para escanear Protocolos de Internet (IPs) a URLs mediante su Dominio.")
    print(Fore.GREEN + "  | by: Rootr - MortenTod")
    print(Fore.GREEN + "  | Uso educativo.\n")
if __name__ == "__main__":
    hawk_banner()
    
    efecto("[*] Iniciando modulo de reconocimiento")  
    slow_print("[*] Listo.\n", 0.03)

    try:
        my_url = input(Fore.WHITE + "SkyHawk > Escriba su dominio aquí: " + Style.RESET_ALL)
        print("   ")
        efecto("[+] Encontrando dominio")
        slow_print("\n[+] Dominio encontrado.", 0.03)

        my_ip = socket.gethostbyname(my_url)

        print("\n" + Fore.GREEN + Style.BRIGHT + "════════════════════════════════════")
        print(Fore.GREEN + " Dominio : " + Fore.WHITE + my_url)
        print(Fore.GREEN + " Respuesta de IP : " + Fore.WHITE + Style.BRIGHT + my_ip)
        print(Fore.GREEN + Style.BRIGHT + "════════════════════════════════════\n")

        slow_print("[ ✓ ] Operación completada con éxito.", 0.03, Fore.CYAN)
        print("            ")

    except socket.gaierror:
        slow_print("[ ! ] Error: Dominio no encontrado.", 0.03, Fore.RED)
    except KeyboardInterrupt:
        slow_print("\n[ ! ] Interrupción por usuario.", 0.03, Fore.RED)