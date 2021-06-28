class person:
    def __init__(self, nama, umur, tinggi, hobi):
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi
        self.hobi = hobi
    def greet(self):
        print('Nama saya adalah', self.nama, 'saat ini saya berumur', self.umur,'dan tinggi', self.tinggi, 'serta memiliki hobi', self.hobi)

user = person('Hammam', '23', '69.25', 'bermain game')
user.greet()