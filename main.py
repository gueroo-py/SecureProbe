import socket
import requests

# Puertos comunes a escanear
COMMON_PORTS = [80, 443, 21, 22, 3306, 8080, 8443]

def resolve_host(target):
    """ Intenta obtener la dirección IP del dominio (IPv4 o IPv6) """
    try:
        # Si el usuario proporciona una IPv6 directamente
        if ":" in target:
            return target  # Retorna la IPv6 directamente
        return socket.gethostbyname(target)  # IPv4
    except socket.gaierror:
        try:
            return socket.getaddrinfo(target, None, socket.AF_INET6)[0][4][0]  # IPv6
        except Exception as e:
            print(f"❌ Error resolviendo la IP: {e}")
            return None

def scan_ports(target):
    """ Escanea los puertos abiertos en la IP del host """
    open_ports = []
    for port in COMMON_PORTS:
        try:
            sock = socket.socket(socket.AF_INET6 if ":" in target else socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except Exception as e:
            print(f"⚠️ Error escaneando el puerto {port}: {e}")
    return open_ports

def check_sql_injection(target):
    """ Verifica si el sitio es vulnerable a SQL Injection """
    test_url = f"http://{target}/?id=1' OR '1'='1"
    try:
        response = requests.get(test_url)
        if "sql" in response.text.lower() or "database" in response.text.lower():
            return True
    except:
        return False
    return False

def check_xss(target):
    """ Verifica si el sitio es vulnerable a XSS """
    test_url = f"http://{target}/?q=<script>alert('XSS')</script>"
    try:
        response = requests.get(test_url)
        if "<script>alert('XSS')</script>" in response.text:
            return True
    except:
        return False
    return False

def main():
    print("🔍 Escáner de Seguridad Web")
    target = input("Ingrese la URL del sitio web o dirección IP (sin http/https): ").strip()

    resolved_ip = resolve_host(target)
    if not resolved_ip:
        print("❌ No se pudo resolver la dirección IP.")
        return
    
    print(f"\n🔗 Dirección IP: {resolved_ip}")

    print("\n🔎 Escaneando puertos abiertos...")
    open_ports = scan_ports(resolved_ip)
    if open_ports:
        print(f"✅ Puertos abiertos detectados: {open_ports}")
    else:
        print("✅ No se detectaron puertos abiertos en los escaneados.")

    print("\n🔍 Buscando vulnerabilidades...")

    if check_sql_injection(target):
        print("🚨 Vulnerabilidad detectada: **SQL Injection**")
        print("💡 **Solución:** Utiliza consultas preparadas (Prepared Statements) y sanitiza las entradas del usuario.")
    else:
        print("✅ No se detectó SQL Injection.")

    if check_xss(target):
        print("🚨 Vulnerabilidad detectada: **Cross-Site Scripting (XSS)**")
        print("💡 **Solución:** Escapa caracteres especiales y usa Content Security Policy (CSP).")
    else:
        print("✅ No se detectó XSS.")

    print("\n🔚 Escaneo finalizado.")

if __name__ == "__main__":
    main()
