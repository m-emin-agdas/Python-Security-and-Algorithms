import socket

def basit_port_tarayici(hedef_ip, port_listesi):
    """Belirtilen hedef IP üzerindeki kritik portların açık olup olmadığını kontrol eder."""
    print(f"[*] {hedef_ip} adresi için tarama başlatılıyor...\n")
    
    for port in port_listesi:
        # Bir TCP soketi oluşturuyoruz
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # 1 saniye içinde cevap gelmezse geç
        
        # Bağlantı denemesi (0 dönerse başarılıdır)
        sonuc = s.connect_ex((hedef_ip, port))
        
        if sonuc == 0:
            print(f"[+] Port {port}: AÇIK (Potansiyel Zafiyet Noktası)")
        else:
            print(f"[-] Port {port}: Kapalı")
            
        s.close()

# Test Edelim (Sadece yerel ağda veya izinli sistemlerde test edilmelidir)
kritik_portlar = [21, 22, 80, 443, 3389]
basit_port_tarayici("127.0.0.1", kritik_portlar)