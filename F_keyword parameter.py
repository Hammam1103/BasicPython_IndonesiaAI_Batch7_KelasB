x = str(input('Masukkan nama anda: '))
y = str(input('Masukkan umur anda: '))
z = str(input('Masukkan tinggi anda: '))
def user(nama, umur, tinggi):
    print('Hello ' + nama)
    print('Anda berumur: ' + umur)
    print('Tinggi anda: ' + tinggi)
user(nama=x, umur=y, tinggi=z)