class Mahasiswa:
    def __init__(self, nama, nim, umur):
        self.nama = nama
        self.nim = nim
        self.umur = umur

    def __str__(self):
        return f"Nama saya adalah {self.nama}, dan NIM saya adalah {self.nim}"
    
    def tahunlahir(self):
        return 2023 - self.umur
    
    def tahunangkatan(self):
        return f"{self.nama}, mahasiswa angkatan 20{self.nim[:2]}"

saya = Mahasiswa("sri", "2207027", 19)
print("Tahun lahir saya adalah", saya.tahunlahir())
print("saya ", saya.tahunangkatan())

#Tahun lahir saya adalah 2004
#saya  sri, mahasiswa angkatan 2022
