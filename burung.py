from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print("Jenis\t\t : ", self.jenis, 
              "\nBunyi \t\t : ", self.bunyi)

gereja = Burung("Gereja", "uduk", "cibinong", "bertelur", "batik jawa", "oweowe")
gereja.cetak_burung()
print("=========================================")
pipit = Burung("Pipit", "nasi", "depok", "bertelur", "baju", "angangang")
pipit.cetak_burung()