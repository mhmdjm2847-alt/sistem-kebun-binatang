qprint("		=[ KEBUN BINATANG PY]=		")
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
        print("Burung bertahan dari mangsa")
    #function kedua

bubut = Burung("butkantut","Bubut hutan","belalang")
print(bubut.__dict__)
bubut.berburu="belalang"
print(bubut.berburu)
