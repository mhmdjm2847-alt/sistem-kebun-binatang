class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def info(self):
        print(f"Nama hewan: {self.nama}")


harimau = Hewan("Harimau")
harimau.info()
