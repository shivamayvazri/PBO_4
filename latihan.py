class mobil:
    def __init__(self, warna, tahun, merk):
        self.warna = warna
        self.tahun = tahun
        self.merk = merk 

    def printname(self):
        print(self.warna)
        print(self.tahun)
        print(self.merk)

class suv(mobil):
    def __init__(self, warna, tahun, merk):
        mobil.__init__(self, warna, tahun, merk)
        self.produk = "Fortuner"

    def tampilansuv(self):
        print("Jenis SUV : ", self.produk)
        print("Merk      : ", self.merk)
        print("Warna     : ", self.warna)
        print("Tahun     : ", self.tahun)

class mpv(mobil):
    def __init__(self, warna, tahun, merk):
        mobil.__init__(self, warna, tahun, merk)
        self.produk = "Grandmax"

    def tampilanmpv(self):
        print("Jenis MPV : ", self.produk)
        print("Merk      : ", self.merk)
        print("Warna     : ", self.warna)
        print("Tahun     : ", self.tahun)

x = suv("Merah", 2021, "Toyota")
y = mpv("Hitam", 2019, "Suzuki")
z = mpv("Hitam", 2020, "Suzuki")

x.tampilansuv()
print("=======================")
y.tampilanmpv()
print("=======================")
z.tampilanmpv()