a = float(input("Masukkan nilai ujian teori: "))
b = float(input("Masukkan nilai ujian praktik: "))

if a >= 70 and b >= 70:
    print("Selamat, anda lulus")
elif a < 70 and b >= 70:
    print("Anda lulus ujian praktik, namun harus mengulang ujian teori")
elif a >= 70 and b < 70 :
    print("Anda lulus ujian teori, namun harus mengulang ujian praktik")
else:
    print("Anda tidak lulus ujian, dan harus mengulang ujian teori dan praktik")