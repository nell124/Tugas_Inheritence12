from Animal import Animal

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi

    def cetak_ikan(self):
        super().cetak(),
        print("Jenis \t: ", self.jenis, 
              "\nBunyin  : ", self.bunyi)

lele = Ikan("lele", "air", "cibinong", "beranak", "panjang", "blukbluk")
lele.cetak_ikan()
print("=========================================")
cupang = Ikan("cupang", "donat", "depok", "bertelur", "sawah", "rawr")
cupang.cetak_ikan()