def basarisiz_giris_tespiti(log_dosyasi_yolu):
    """Bir sunucu log dosyasındaki 'Failed password' (Başarısız giriş) denemelerini sayar."""
    hata_sayisi = 0
    supheli_ipler = []

    try:
        with open(log_dosyasi_yolu, "r") as dosya:
            satirlar = dosya.readlines()
            
            for satir in satirlar:
                # Eğer satırda başarısız giriş ibaresi varsa yakala
                if "Failed password" in satir:
                    hata_sayisi += 1
                    # Satırı boşluklardan bölüp IP adresinin olduğu kısmı (genelde 11. sütun) al
                    parcalar = satir.split()
                    if len(parcalar) > 10:
                        ip_adresi = parcalar[10]
                        if ip_adresi not in supheli_ipler:
                            supheli_ipler.append(ip_adresi)
                            
        print(f"[*] Analiz Tamamlandı. Toplam Başarısız Giriş: {hata_sayisi}")
        print(f"[!] Tespit Edilen Şüpheli IP'ler: {supheli_ipler}")
        
    except FileNotFoundError:
        print("Hata: Log dosyası bulunamadı. Lütfen yolu kontrol edin.")

# (Not: Çalıştırmak için aynı klasörde 'auth.log' adında sahte bir metin dosyası olmalıdır)
# basarisiz_giris_tespiti("auth.log")