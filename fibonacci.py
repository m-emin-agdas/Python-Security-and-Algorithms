def fibonacci_uret(n):
    """
    Girilen 'n' sayısına kadar (n adet) Fibonacci dizisi üretir.
    Kural: Her sayı, kendisinden önceki iki sayının toplamıdır.
    """
    # Eğer kullanıcı 0 veya negatif girerse boş liste dön
    if n <= 0:
        return []
    # Eğer 1 girerse sadece ilk elemanı dön
    elif n == 1:
        return [0]

    # Dizinin temelini atıyoruz (İlk iki sayı her zaman 0 ve 1'dir)
    dizi = [0, 1]
    
    # Kalan sayıları bulmak için 2. indeksten başlayıp 'n' kadar dönüyoruz
    for _ in range(2, n):
        # Son iki elemanı topla ve yeni sayıyı bul
        yeni_sayi = dizi[-1] + dizi[-2]
        
        # Bulduğun yeni sayıyı listeye ekle
        dizi.append(yeni_sayi)
        
    return dizi

# Test Edelim
print("İlk 10 Fibonacci sayısı:")
print(fibonacci_uret(10)) 
# Beklenen Çıktı: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]