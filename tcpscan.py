import socket

ip = input("[+] Introduce la IP --> ")

print("[+] Iniciando el escaneo de la ", ip,)

try:
    for ports in range(0,65535):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        estado = s.connect_ex((ip,ports))
        if estado ==0:
            print("[+] Los puertos ",ports," ABIERTOS!!!")
            continue
        else:
            pass
except KeyboardInterrupt:
    print("[-] SALIENDO!!!")

except socket.gaierror:
    print("[-] ERROR RESOLVIENDO HOST!!!")

except socket.error:
    print("[-] SERVIDOR NO RESPONDE!!!")

finally:
    print("[!] GRACIAS POR USAR ESTE SCRIPT")