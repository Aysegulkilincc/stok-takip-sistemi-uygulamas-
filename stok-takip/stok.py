class Urun:
    # Ürün sınıfı ürün bilgilerini tutar
    def __init__(self, urun_id, ad, stok):
        self.urun_id = urun_id
        self.ad = ad
        self.stok = stok

    def bilgileri_goster(self):
        # Ürün bilgilerini ekrana yazdırır
        return f"Ürün ID: {self.urun_id}, Ad: {self.ad}, Stok: {self.stok}"

    def stok_guncelle(self, miktar):
        # Ürünün stoğunu günceller
        self.stok += miktar
        print(f"Stok güncellendi. Güncel stok: {self.stok}")


class Siparis:
        # Sipariş sınıfı sipariş bilgilerini tutar
    def __init__(self, siparis_id, urun, miktar):
        self.siparis_id = siparis_id
        self.urun = urun
        self.miktar = miktar

    def siparis_detaylari(self):
         # Sipariş detaylarını ekrana yazdırır
        return f"Sipariş ID: {self.siparis_id}, Ürün: {self.urun.ad}, Miktar: {self.miktar}"


class StokTakipSistemi:
    # Stok Takip Sistemi sınıfı ürün ve siparişlerin yönetildiği sınıftır
    def __init__(self):
        self.urunler = []
        self.siparisler = []
        self.siparis_sayaci = 1

    def urun_ekle(self, urun):
        # Yeni bir ürün ekler
        self.urunler.append(urun)

    def urunleri_listele(self):
        # Ürünleri listeler
        for urun in self.urunler:
            print(urun.bilgileri_goster())

    def siparis_olustur(self, urun_id, miktar):
         # Sipariş oluşturur
        urun = self.urun_bul(urun_id)
        if urun:
            if urun.stok >= miktar:
                urun.stok -= miktar
                siparis = Siparis(self.siparis_sayaci, urun, miktar)
                self.siparisler.append(siparis)
                self.siparis_sayaci += 1
                print("Sipariş oluşturuldu.")
            else:
                print("Stok yetersiz")
        else:
            print("Ürün bulunamadı.")

    def stok_guncelle(self, urun_id, miktar):
          # Ürün stoğunu günceller
        urun = self.urun_bul(urun_id)
        if urun:
            urun.stok_guncelle(miktar)
        else:
            print("Ürün bulunamadı.")

    def siparisleri_listele(self):
         # Tüm siparişleri listeler
        for siparis in self.siparisler:
            print(siparis.siparis_detaylari())

    def urun_bul(self, urun_id):
        # Ürün ID'sine göre ürünü bulur
        for urun in self.urunler:
            if urun.urun_id == urun_id:
                return urun
        return None

    def menu(self):
        # Kullanıcıya menü sunar
        while True:
            print("\n     STOK TAKİP MENÜSÜ     ")
            print("1 - Ürünleri Listele")
            print("2 - Yeni Ürün Ekle")
            print("3 - Stok Güncelle")
            print("4 - Sipariş Oluştur")
            print("5 - Siparişleri Listele")
            print("6 - Çıkış yap")
            
            try:
                secim = int(input("Ne yapmak istiyorsun? (Seçim yap: 1-6): "))
            except ValueError:
                print("Hatalı giriş yaptın, rakam kullan.")
                continue

            if secim == 1:
                self.urunleri_listele()
            elif secim == 2:
                urun_id = int(input("Ürün ID gir: "))
                ad = input("Ürün adı gir: ")
                stok = int(input("Başlangıç stok gir: "))
                urun = Urun(urun_id, ad, stok)
                self.urun_ekle(urun)
                print(f"{ad} ürünü başarıyla eklendi!")
            elif secim == 3:
                urun_id = int(input("Stok güncellemesi için ürün ID gir: "))
                miktar = int(input("Eklenecek stok miktarı gir (eksi de verebilirsin): "))
                self.stok_guncelle(urun_id, miktar)
            elif secim == 4:
                urun_id = int(input("Sipariş için ürün ID gir: "))
                miktar = int(input("Kaç tane sipariş etmek istiyorsun?: "))
                self.siparis_olustur(urun_id, miktar)
            elif secim == 5:
                self.siparisleri_listele()
            elif secim == 6:
                print("Çıkış yapılıyor")
                break
            else:
                print("Yanlış seçim yaptın. Tekrar dene.")

stok_sistemi = StokTakipSistemi()

stok_sistemi.urun_ekle(Urun(1, "Laptop", 28))
stok_sistemi.urun_ekle(Urun(2, "Telefon", 12))
stok_sistemi.urun_ekle(Urun(3, "Tulaklık", 50))
stok_sistemi.urun_ekle(Urun(4, "Şarj aleti", 30))
stok_sistemi.urun_ekle(Urun(5, "Mouse", 15))
stok_sistemi.urun_ekle(Urun(6, "Tablet", 10))
stok_sistemi.urun_ekle(Urun(7, "Klavye", 37))
stok_sistemi.urun_ekle(Urun(8, "Televizyon", 9))
stok_sistemi.urun_ekle(Urun(9, "Hoparlör", 26))


stok_sistemi.menu()
