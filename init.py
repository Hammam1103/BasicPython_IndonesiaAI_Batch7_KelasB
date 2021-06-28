class hewan:
    def __init__(self, kaki, gigi, makanan):
        self.kaki = kaki
        self.gigi = gigi
        self.makanan = makanan

macan = hewan(4, 'punya taring', 'daging')
kelinci = hewan(4, 'tidak punya taring', 'tumbuhan')
print(macan.kaki)
print(kelinci.makanan)