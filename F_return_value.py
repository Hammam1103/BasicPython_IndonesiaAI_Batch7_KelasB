#def nama(Hammam):
#    return 10 * Hammam
#print(nama(5))
#print(nama(10))


p = int(input('Masukkan panjang benda: '))
l = int(input('Masukkan lebar benda: '))
def fungsi(p,l):
    Luas = p*l
    Teks = 'Luas persegi panjang dengan panjanga {} cm dan lebar {} cm adalah {} cm\u00b2.'.format(p, l, Luas)
    return Teks
print(fungsi(p,l))