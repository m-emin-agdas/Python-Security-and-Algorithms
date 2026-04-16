import socket

def banner_yakala(ip, port):
    """Hedef servisin (örneğin web veya ftp) versiyon bilgisini (banner) çeker."""
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        
        # HTTP için özel bir istek göndermemiz gerekir
        if port == 80 or port == 443:
            istek = "HEAD / HTTP/1.0\r\n\r\n"
            s.send(istek.encode())
            
        banner = s.recv(1024).decode().strip()
        print(f"[+] {ip}:{port} üzerinden alınan bilgi:\n{banner}\n")
    except Exception as e:
        print(f"[-] {ip}:{port} bağlantı hatası veya banner okunamadı: {e}")
    finally:
        s.close()

# Test Edelim (Diyanet'in herkese açık IP'si veya bir eğitim laboratuvarı)
# banner_yakala("hedef_ip_adresi", 80)