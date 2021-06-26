b = {
    "Nama": "Hammam",
    "Umur": 23,
    "Universitas": "Brawijaya"
}
print(b["Nama"])
print(b)
b["Nama"]="Ham"
print(b)

b = []
for x in range(1):
    nama = input("Masukkan nama anda: ")
    umur = int(input("Masukkan umur anda: "))
    universitas = input('Masukkan universitas anda: ')
    data = {
        "Nama" : nama,
        "Umur" : umur,
        "Universitas" : universitas
    }
    b.append(data)
for x in b:
    print("Nama mahasiswa: ",x["Nama"])
    print("Umur mahasiswa: ",x["Umur"])
    print("Univeritas: ",x["Universitas"])