def siber_fizzbuzz():
    """
    1'den 100'e kadar sayar. 
    3'ün katlarında 'Siber', 5'in katlarında 'Güvenlik', 
    15'in katlarında 'SiberGüvenlik' yazdırır.
    """
    for sayi in range(1, 101):
        # En dar koşul (hem 3'e hem 5'e tam bölünme) en başa yazılmalıdır!
        if sayi % 3 == 0 and sayi % 5 == 0:
            print("SiberGüvenlik")
        elif sayi % 3 == 0:
            print("Siber")
        elif sayi % 5 == 0:
            print("Güvenlik")
        else:
            print(sayi)

# Test Edelim
siber_fizzbuzz()