class hp:
    def __init__(self, warna, tahun, nama):
        self.warna = warna
        self.tahun = tahun
        self.nama = nama

    def printname(self):
        print(self.warna)
        print(self.tahun)
        print(self.nama)

class android(hp):
    def __init__(self, warna, tahun, nama):
        hp.__init__(self, warna, tahun, nama)
        self.produk = "Oppo"

    def tampilanandroid(self):
        print("Jenis HP : ", self.produk)
        print("Nama     : ", self.nama)
        print("Warna    : ", self.warna)
        print("Tahun    : ", self.tahun)

class ip(hp):
    def __init__(self, warna, tahun, nama):
        hp.__init__(self, warna, tahun, nama)
        self.produk = "Iphone"

    def tampilanip(self):
        print("Jenis HP : ", self.produk)
        print("Nama     : ", self.nama)
        print("Warna    : ", self.warna)
        print("Tahun    : ", self.tahun)

a = android("Gold", 2018, "Oppo A37f")
b = ip("Rose Gold", 2021, "Iphone 12 pro")
c = android("Grey", 2020, "Oppo 2020")
d = ip("White", 2019, "Iphone 11")
e = ip("Black", 2017, "Iphone 10")

a.tampilanandroid()
print("=======================")
b.tampilanip()
print("=======================")
c.tampilanandroid()
print("=======================")
d.tampilanip()
print("=======================")
e.tampilanip()