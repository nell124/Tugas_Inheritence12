class person:
    def __init__(self, nama, umur, jeniskelamin):
        self.nama = nama
        self.umur = umur
        self.jeniskelamin = jeniskelamin

    def jalan(self):
        print(f"{self.nama} bisa berjalan")

    def ngomong(self):
        print(f"Dia berbicara karena dia {self.jeniskelamin}")


class Supir(person):
    def __init__(self, nama, umur, jeniskelamin, sim):
        super().__init__(nama, umur, jeniskelamin)
        self.sim = sim 

    def nyupir(self):
        print(f"{self.nama} bisa nyupir karena memiliki SIM {self.sim}")



class Mahasiswa(person):
    def __init__(self, nama, umur, jeniskelamin, nim):
        super().__init__(nama, umur, jeniskelamin)
        self.nim = nim

    def belajar(self):
        print(f"{self.nama} sedang belajar dengan nim {self.nim}")

bayu = person("bayu", 20, "Laki-Laki")
bayu.jalan()
bayu.ngomong()

andi = Supir("andi", 30, "Laki-Laki", "A")
andi.nyupir()

bunga = Mahasiswa("bunga", 20, "perempuan", "132452")
bunga.belajar()
bunga.belajar()