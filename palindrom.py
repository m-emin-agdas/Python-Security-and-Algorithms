def palindrom_mu(kelime):
    # Kelimedeki boşlukları silip küçük harfe çeviriyoruz (Temiz veri her şeydir)
    kelime = kelime.replace(" ", "").lower()
  
    sol = 0			# İlk harfin indeksi
    sag = len(kelime) - 1	# Son harfin indeksi

    # İşaretçiler ortada buluşana kadar veya birbirini geçene kadar dön
    while sol < sag:
	# Harfler eşleşmiyorsa anında bitir ve False dön
	    if kelime[sol] != kelime[sag]:
	        return False

	# Harfler aynıysa birer adım içeri kay
	    sol += 1
	    sag -= 1

    # Döngü sorunsuz bittiyse kelime palindromdur
    return True

# Test Edelim
print(palindrom_mu("kayak"))	# Çıktı: True
print(palindrom_mu("diyanet"))  # Çıktı: False