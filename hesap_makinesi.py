def topla(x, y):
    """İki sayıyı toplar."""
    return x + y

def cikar(x, y):
    """İki sayıyı çıkarır."""
    return x - y

def carp(x, y):
    """İki sayıyı çarpar."""
    return x * y

def bol(x, y):
    """İki sayıyı böler, sıfıra bölme hatasını kontrol eder."""
    if y == 0:
        raise ZeroDivisionError("Bir sayı sıfıra bölünemez!")
    return x / y

def sayi_al(mesaj):
    """Kullanıcıdan geçerli bir sayı girişi alır."""
    while True:
        try:
            return float(input(mesaj))
        except ValueError:
            print("Geçersiz giriş! Lütfen geçerli bir sayı girin.\n")

def menu_goster():
    print("=" * 30)
    print("       HESAP MAKİNESİ")
    print("=" * 30)
    print("1. Toplama (+)")
    print("2. Çıkarma (-)")
    print("3. Çarpma (*)")
    print("4. Bölme (/)")
    print("5. Çıkış (q)")
    print("=" * 30)

def main():
    while True:
        menu_goster()
        secim = input("Lütfen bir işlem seçin (1-5 veya q): ").strip().lower()

        if secim in ('5', 'q', 'cikis', 'çıkış'):
            print("Hesap makinesinden çıkılıyor. İyi günler!")
            break

        if secim not in ('1', '2', '3', '4'):
            print("Geçersiz seçim! Lütfen 1-5 arasında bir seçenek girin.\n")
            continue

        sayi1 = sayi_al("Birinci sayıyı girin: ")
        sayi2 = sayi_al("İkinci sayıyı girin: ")

        try:
            if secim == '1':
                sonuc = topla(sayi1, sayi2)
                sembol = "+"
            elif secim == '2':
                sonuc = cikar(sayi1, sayi2)
                sembol = "-"
            elif secim == '3':
                sonuc = carp(sayi1, sayi2)
                sembol = "*"
            elif secim == '4':
                sonuc = bol(sayi1, sayi2)
                sembol = "/"

            # Tam sayıları .0 olmadan temiz göstermek için kontrol
            sayi1_str = int(sayi1) if sayi1.is_integer() else sayi1
            sayi2_str = int(sayi2) if sayi2.is_integer() else sayi2
            sonuc_str = int(sonuc) if isinstance(sonuc, float) and sonuc.is_integer() else sonuc

            print(f"\nSonuç: {sayi1_str} {sembol} {sayi2_str} = {sonuc_str}\n")

        except ZeroDivisionError as e:
            print(f"\nHata: {e}\n")

        devam = input("Başka bir işlem yapmak istiyor musunuz? (e/h): ").strip().lower()
        if devam == 'h':
            print("Hesap makinesinden çıkılıyor. İyi günler!")
            break
        print()

if __name__ == "__main__":
    main()

