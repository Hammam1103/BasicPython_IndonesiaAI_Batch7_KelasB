Daftar_kontak = []
x = 0

while x == 0 :
    print('Halo, selamat datang kembali!')
    print('--Menu--')
    print('1. Daftar kontak')
    print('2. Tambah kontak baru')
    print('3. Keluar')
    print()

    menu = int(input('Pilih menu'))
    y = menu
    def tambah_kontak():
        for i in range(1):
            nama = input('Nama: ')
            no_telp = input('No. Telp.: ')
            data_kontak = {
                'Nama' : nama,
                'No. Telp.' : no_telp
            }
        Daftar_kontak.append(data_kontak)
        print('Kontak baru berhasil ditambahkan')
        print()
    def kontak_baru():
        for i in Daftar_kontak:
            print('Nama: ', i['Nama'])
            print('No. Telp.: ', i['No. Telp.'])
            print()
        
    a = 0
    if menu == 1:
        while True:
            kontak_baru()
            pilihan = str(input('Apakah anda yakih sudah selesai dan menyimpannya? (Yes/No)'))
            if pilihan == 'Yes':
                break
    elif menu == 2:
        print(tambah_kontak())
    elif menu == 3:
        print('Selesai, sampai jumpa kembai!')
        break
    else:
        print('Menu tidak tersedia!')

    if y == 3:
        x = 1