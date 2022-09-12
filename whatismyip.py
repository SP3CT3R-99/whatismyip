from requests import get
import time
import socket
try:
    ip = get('https://api.myip.com').json()
    device_name = socket.gethostname()
    local_ip = socket.gethostbyname(device_name)

    print("""
░██╗░░░░░░░██╗██╗░░██╗░█████╗░████████╗  ██╗░██████╗  ███╗░░░███╗██╗░░░██╗  ██╗██████╗░
░██║░░██╗░░██║██║░░██║██╔══██╗╚══██╔══╝  ██║██╔════╝  ████╗░████║╚██╗░██╔╝  ██║██╔══██╗
░╚██╗████╗██╔╝███████║███████║░░░██║░░░  ██║╚█████╗░  ██╔████╔██║░╚████╔╝░  ██║██████╔╝
░░████╔═████║░██╔══██║██╔══██║░░░██║░░░  ██║░╚═══██╗  ██║╚██╔╝██║░░╚██╔╝░░  ██║██╔═══╝░
░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║░░░██║░░░  ██║██████╔╝  ██║░╚═╝░██║░░░██║░░░  ██║██║░░░░░
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  ╚═╝╚═════╝░  ╚═╝░░░░░╚═╝░░░╚═╝░░░  ╚═╝╚═╝░░░░░
    """)
    time.sleep(1)
    print(f"[+] your local IP address is: {local_ip}")
    print(f"[+] your public IP address is: {ip.get('ip')}")
    print(f"[+] your Country is: {ip.get('country')}")
    print(f"[+] Top level Domain of Country is: {ip.get('cc')}")


except NameError as err:
    print("[+] required modules missing ..")
except:
    print("[+] Connection time out ..")


