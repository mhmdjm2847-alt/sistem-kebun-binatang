print("		=[ KEBUN BINATANG PY]=		")
print("		======================		")

from abc import ABC,abstractmethod
class Hewan(ABC):
    def __init__(self,nama,jenis):
        self.nama = nama
        self.jenis = jenis
    #attribut wajib untuk setiap subclass
    @abstractmethod
    def berburu(self):
        pass
    def bertahan(self):
        pass

class Burung(Hewan):
    def __init__(self,nama,jenis,makan):
        super().__init__(nama,jenis)
        self.makan = makan
    def berburu(self):
        print("Burung berburu makan")
    #function pertama
    def bertahan(self):
        print("Burung bertahan dengan terbang")
    #function kedua

class Ikan(Hewan):
    def __init__(self,nama,jenis,hidup,makan):
        self.nama = nama
        self.jenis = jenis
        self.hidup = hidup
        self.makan = makan

    def berburu(self):
        print("berburu binatang laut")

    def bertahan(self):
        print("bertahan dengan berenang")

bubut = Burung("butkantut","Bubut hutan","belalang")
print(bubut.__dict__)
bubut.berburu="belalang"
print(bubut.berburu)
#obejek class Ikan
hiu = Ikan("Hieyong","Hiu paus","laut","ubur ubur")
print(hiu.__dict__)
hiu.berburu()
hiu.bertahan()
hiu.berburu= "tidak gak berburu soalnya jinak"
hiu.bertahan="dengan bawa golok"
print(hiu.berburu)
print(hiu.bertahan)
