def en_buyugu_bul(sayi_listesi):
    """Bir listedeki en büyük sayıyı hazır fonksiyon kullanmadan bulur."""
    if not sayi_listesi:
        return None
    
    # Listenin ilk elemanını şimdilik en büyük kabul ediyoruz
    gecici_en_buyuk = sayi_listesi[0]
    
    # Listedeki her bir sayıya tek tek bakıyoruz
    for sayi in sayi_listesi:
        if sayi > gecici_en_buyuk:
            gecici_en_buyuk = sayi  # Daha büyüğünü bulursak tacı ona devrediyoruz
            
    return gecici_en_buyuk

# Test Edelim
sayilar = [12, 45, 7, 99, 23, 8]
print(f"Listedeki en büyük sayı: {en_buyugu_bul(sayilar)}") # Çıktı: 99